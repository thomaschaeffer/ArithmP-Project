import click

from arithmp.parser import Parser


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
    else:
        return _command(expression)
    
    



if __name__ == "__main__":
    main()

