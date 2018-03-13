import ip_finder
import asyncio
import asyncssh


async def update_client(ip, simple_name=None, username='pi', password=None):
    await ssh_run_command(ip, simple_name, username, password, 'sudo apt-get update && sudo apt-get upgrade -y')


async def ssh_run_command(ip, simple_name, username, password, command):
    if simple_name:
        name = "{} ({})".format(simple_name, ip)
    else:
        name = ip

    print("Connecting to {} and executing Update...".format(name))

    try:
        async with asyncssh.connect(ip, username=username, password=password, known_hosts=None) as conn:
            result = await conn.run(command)

        to_print = result.stdout
        to_print = str(to_print).strip()

        to_print = "\n{}\nExit-Status: {}".format(to_print, result.exit_status)

        if result.exit_status != 0:
            to_print = to_print + '\n' + result.stderr

        to_print = to_print.replace('\n', '\n\t')

        print("{}: {}".format(name, to_print))
    except asyncssh.misc.DisconnectError as e:
        print("Cannot connect to {}: {}".format(name, e.reason))


if __name__ == '__main__':
    pis = ip_finder.find_pis()
    futures = [update_client(pi.ip, simple_name=pi.hostname) for pi in pis]
    asyncio.get_event_loop().run_until_complete(
        asyncio.gather(*futures)
    )
