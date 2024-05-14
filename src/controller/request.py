import os
import click
import asyncio
import settings

from click.core import Context
from time import perf_counter
from collections import ChainMap
from icecream import ic

from src.utils import Stream, Annotations
from src.services.request import *

class Request:

    @click.group()
    @click.option('--s3', '-s3', is_flag=True, default=False)
    @click.option('--kafka', '-s3', is_flag=True, default=False)
    @click.option('--thread', '-th',  is_flag=True, default=False)
    @click.option('--save', '-sv',  is_flag=True, default=False)
    @click.option('--beanstalk-host', '-bh', default=settings.BEANSTALK["host"])
    @click.option('--beanstalk-port', '-bh', default=settings.BEANSTALK["port"])
    @click.option('--beanstalk-tube', '-bt', required=True)
    @click.pass_context
    def task(ctx: Context, **kwargs):
        ctx.obj = kwargs
        ...

    @staticmethod
    @task.command('getDayTrends')
    @click.pass_context
    def getDayTrends(ctx: Context) -> None:

        imdy = GetDayTrends(ctx.obj)
        imdy.main()

        ...