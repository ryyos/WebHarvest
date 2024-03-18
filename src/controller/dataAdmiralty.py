import os
import click
import asyncio

from click.core import Context
from time import perf_counter
from collections import ChainMap
from icecream import ic

from src.utils import Stream, Annotations
from src.services.dataAdmiralty import *

class DataAdmiralty:

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
    @task.command('mybank')
    @click.pass_context
    def myBank(ctx: Context) -> None:

        my = MayBank(ctx.obj)
        my.main()

        ...

    @staticmethod
    @task.command('uob')
    @click.pass_context
    def uob(ctx: Context) -> None:

        u = Uob(ctx.obj)
        u.main()

        ...

    @staticmethod
    @task.command('ocbc')
    @click.pass_context
    def ocbc(ctx: Context) -> None:

        ocbc = Ocbc(ctx.obj)
        ocbc.main()

        ...

    @staticmethod
    @task.command('trop', help='The Religion OfP eace')
    @click.option('--all', '-a', is_flag=True, default=False, help='want to stream or take all')
    @click.option('--no-update', '-no', is_flag=True, default=False, help='Update date stream or not')
    @click.pass_context
    def trop(ctx: Context, **kwargs) -> None:

        trop = TheReligionOfPeace(ChainMap(ctx.obj, kwargs))
        trop.main()

        ...

    @staticmethod
    @task.command('arthagraha')
    @click.pass_context
    def arthagraha(ctx: Context) -> None:

        arthagraha = Arthagraha(ctx.obj)
        arthagraha.main()
        ...

    @staticmethod
    @task.command('bankbba')
    @click.pass_context
    def bankbba(ctx: Context) -> None:

        bankbba = Bankbba(ctx.obj)
        bankbba.main()
        ...

    @staticmethod
    @task.command('jtrustbank')
    @click.pass_context
    def jtrustbank(ctx: Context) -> None:

        jtrustbank = Jtrustbank(ctx.obj)
        jtrustbank.main()
        ...

    @staticmethod
    @Annotations.stopwatch
    @task.command('bankmayapada')
    @click.pass_context
    def bankmayapada(ctx: Context) -> None:

        bankmayapada = Bankmayapada(ctx.obj)
        asyncio.run(bankmayapada.main())
        ...

    @staticmethod
    @Annotations.stopwatch
    @task.command('boiindonesia')
    @click.pass_context
    def boiindonesia(ctx: Context) -> None:

        boiindonesia = Boiindonesia(ctx.obj)
        asyncio.run(boiindonesia.main())
        ...

    @staticmethod
    @Annotations.stopwatch
    @task.command('bankmuamalat')
    @click.pass_context
    def bankmuamalat(ctx: Context) -> None:

        bankmuamalat = Bankmuamalat(ctx.obj)
        asyncio.run(bankmuamalat.main())
        ...

    @staticmethod
    @Annotations.stopwatch
    @task.command('bankmestika')
    @click.pass_context
    def bankmestika(ctx: Context) -> None:

        bankmestika = Bankmestika(ctx.obj)
        asyncio.run(bankmestika.main())
        ...
        
    @staticmethod
    @Annotations.stopwatch
    @task.command('shinhan')
    @click.pass_context
    def shinhan(ctx: Context) -> None:

        shinhan = Shinhan(ctx.obj)
        asyncio.run(shinhan.main())
        ...

    @staticmethod
    @Annotations.stopwatch
    @task.command('banksinarmas')
    @click.pass_context
    def banksinarmas(ctx: Context) -> None:

        banksinarmas = Banksinarmas(ctx.obj)
        asyncio.run(banksinarmas.main())
        ...

    @staticmethod
    @Annotations.stopwatch
    @task.command('bankganesha')
    @click.pass_context
    def bankganesha(ctx: Context) -> None:

        bankganesha = Bankganesha(ctx.obj)
        bankganesha.main()
        ...
        
    @staticmethod
    @Annotations.stopwatch
    @task.command('icbc')
    @click.pass_context
    def icbc(ctx: Context) -> None:

        icbc = Icbc(ctx.obj)
        icbc.main()
        ...

    @staticmethod
    @Annotations.stopwatch
    @task.command('qnb')
    @click.pass_context
    def qnb(ctx: Context) -> None:

        qnb = Qnb(ctx.obj)
        qnb.main()
        ...