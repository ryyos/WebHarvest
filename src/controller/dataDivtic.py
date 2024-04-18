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

    @staticmethod
    @task.command('geospasial')
    @click.pass_context
    def geospasial(ctx: Context) -> None:

        geo = Geospasial(ctx.obj)
        asyncio.run(geo.main())

        ...
        
    @staticmethod
    @task.command('unodc')
    @click.pass_context
    def unodc(ctx: Context) -> None:

        unodc = Unodc(ctx.obj)
        asyncio.run(unodc.main())

        ...
        
    @staticmethod
    @task.command('worldbank', help='The Religion OfP eace')
    @click.option('--mode', '-m', help='insert mode')
    @click.option('--headless', '-h',  is_flag=True, default=False)
    @click.pass_context
    def world(ctx: Context, **kwargs) -> None:

        world = Worldbank(ChainMap(ctx.obj, kwargs))
        world.main()

        ...