import os
import click

from click.core import Context
from time import perf_counter
from collections import ChainMap
from icecream import ic

from src.utils import Stream
from src.server import S3

class Shared:

    @click.group()
    @click.pass_context
    def task(ctx: Context, **kwargs):
        ctx.obj = kwargs
        ...

    @staticmethod
    @task.command('s3')
    @click.option('--source', '-sc', required=True)
    @click.pass_context
    def myBank(ctx: Context, source: str) -> None:
        S3.local2s3(source)
        ...