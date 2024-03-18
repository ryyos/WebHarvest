import os
import click
import asyncio

from click.core import Context
from time import perf_counter
from collections import ChainMap
from icecream import ic

from src.utils import Stream, Annotations
from src.services.dataDivtic import *

class DataDivtic:

    @click.group()
    @click.option('--s3', '-s3', is_flag=True, default=False)
    @click.option('--kafka', '-s3', is_flag=True, default=False)
    @click.option('--thread', '-th',  is_flag=True, default=False)
    @click.option('--save', '-sv',  is_flag=True, default=False)
    @click.pass_context
    def task(ctx: Context, **kwargs):
        ctx.obj = kwargs
        ...

    @staticmethod
    @task.command('imdi')
    @click.pass_context
    def imdi(ctx: Context) -> None:

        imdy = Imdi(ctx.obj)
        asyncio.run(imdy.main())

        ...