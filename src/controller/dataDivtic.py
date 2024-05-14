import os
import click
import asyncio
import settings

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
    @click.option('--beanstalk-host', '-bh', default=settings.BEANSTALK["host"])
    @click.option('--beanstalk-port', '-bh', default=settings.BEANSTALK["port"])
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
    @task.command('worldbank')
    @click.option('--mode', '-m', help='insert mode')
    @click.option('--headless', '-h',  is_flag=True, default=False)
    @click.pass_context
    def world(ctx: Context, **kwargs) -> None:

        world = Worldbank(ChainMap(ctx.obj, kwargs))
        world.main()

        ...
        
    @staticmethod
    @task.command('ahugoid')
    @click.option('--keyword', '-k', help='insert keyword')
    @click.option('--recaptcha', '-k', help='insert recaptcha token')
    @click.pass_context
    def ahugoid(ctx: Context, **kwargs) -> None:

        ahugoid = Ahugoid(ChainMap(ctx.obj, kwargs))
        ahugoid.main()

        ...
        
    @staticmethod
    @task.command('dephub')
    @click.pass_context
    def dephub(ctx: Context) -> None:

        dephub = Dephub(ctx.obj)
        dephub.main()

        ...
        
    @staticmethod
    @task.command('sipsn')
    @click.pass_context
    def sipsn(ctx: Context) -> None:

        sipsn = Sipsn(ctx.obj)
        sipsn.main()

        ...
        
    @staticmethod
    @task.command('bpsPublikasi')
    @click.pass_context
    def bpsPublikasi(ctx: Context) -> None:

        bpsPublikasi = BpsPublikasi(ctx.obj)
        bpsPublikasi.main()

        ...
        
    @staticmethod
    @task.command('kkp')
    @click.pass_context
    def kkp(ctx: Context) -> None:

        kkp = Kkp(ctx.obj)
        kkp.main()

        ...
        
    @staticmethod
    @task.command('bi')
    @click.option('--mode', '-m', help='insert mode')
    @click.option('--url', '-u', help='insert url')
    @click.option('--category', '-c', help='insert category')
    @click.pass_context
    def bi(ctx: Context, **kwargs) -> None:

        bi = BI(ChainMap(ctx.obj, kwargs))
        bi.main()

        ...