import click

from arithmp.parser import Parser


def _interactive():
    parser = Parser()
    click.echo("Arithmp interactive interpreter: write quit to leave")
    while True:
        expression = input("Input: ")
        if expression == "quit":
            break
        if expression=="":
            continue
        result= parser.parse(expression)
        click.echo(result)
        
def _command(expression: str):
    parser = Parser()
    result = parser.parse(expression)
    click.echo(result)


@click.command()
@click.option("-c","command", type=str,required=False,default=None)
@click.argument("expression", required=False)
def main(command: str |None,expression: str|None):
    if command is not None:
        return _command(command)
    if expression is not None:
        return _command(expression)
    
    return _interactive()



if __name__ == "__main__":
    main()

