import os
import click
import asyncio

from click.core import Context
from time import perf_counter
from collections import ChainMap
from icecream import ic

from src.utils import Stream, Annotations
from src.services.dataIcc import *

class DataIcc:

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
    @task.command('google-reviews')
    @click.option('--url', '-u', required=True, help='insert url')
    @click.option('--worker', '-u', required=True, help='insert count worker')
    @click.pass_context
    def google(ctx: Context, **kwargs) -> None:

        google = GoogleReviews(ChainMap(ctx.obj, kwargs))
        asyncio.run(google.main())

        ...
