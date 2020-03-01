#!/usr/bin/env python
import click

@click.command()
def hello():
    click.echo('Hello World! My name is Kelsey Summey')

if __name__ == '__main__':
    hello()