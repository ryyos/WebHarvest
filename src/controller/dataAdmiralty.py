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
    @click.option('--custom', '-c', is_flag=True, default=False)
    @click.option('--url', '-no')
    @click.option('--year', '-yr')
    @click.option('--start', '-st')
    @click.option('--end', '-e')
    @click.option('--topic', '-t')
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

    @staticmethod
    @Annotations.stopwatch
    @task.command('bankmega')
    @click.pass_context
    def bankmega(ctx: Context) -> None:

        bankmega = Bankmega(ctx.obj)
        bankmega.main()
        ...

    @staticmethod
    @Annotations.stopwatch
    @task.command('bankbsi')
    @click.pass_context
    def bankbsi(ctx: Context) -> None:

        bankbsi = Bankbsi(ctx.obj)
        bankbsi.main()
        ...

    @staticmethod
    @Annotations.stopwatch
    @task.command('kbbukopinsyariah')
    @click.pass_context
    def kbbukopinsyariah(ctx: Context) -> None:

        kbbukopinsyariah = Kbbukopinsyariah(ctx.obj)
        kbbukopinsyariah.main()
        ...

    @staticmethod
    @Annotations.stopwatch
    @task.command('mncbank')
    @click.pass_context
    def mncbank(ctx: Context) -> None:

        mncbank = Mncbank(ctx.obj)
        mncbank.main()
        ...
        
    @staticmethod
    @Annotations.stopwatch
    @task.command('megasyariah')
    @click.pass_context
    def megasyariah(ctx: Context) -> None:

        megasyariah = Megasyariah(ctx.obj)
        megasyariah.main()
        ...

    @staticmethod
    @Annotations.stopwatch
    @task.command('bankindex')
    @click.pass_context
    def bankindex(ctx: Context) -> None:

        bankindex = Bankindex(ctx.obj)
        bankindex.main()
        ...

    @staticmethod
    @Annotations.stopwatch
    @task.command('hibank')
    @click.pass_context
    def hibank(ctx: Context) -> None:

        hibank = Hibank(ctx.obj)
        hibank.main()
        ...
        
    @staticmethod
    @Annotations.stopwatch
    @task.command('ccb')
    @click.pass_context
    def ccb(ctx: Context) -> None:

        ccb = Ccb(ctx.obj)
        asyncio.run(ccb.main())
        ...

    @staticmethod
    @Annotations.stopwatch
    @task.command('dbs')
    @click.pass_context
    def dbs(ctx: Context) -> None:

        dbs = Dbs(ctx.obj)
        dbs.main()
        ...

    @staticmethod
    @Annotations.stopwatch
    @task.command('perdania')
    @click.pass_context
    def perdania(ctx: Context) -> None:

        perdania = Perdania(ctx.obj)
        asyncio.run(perdania.main())
        ...

    @staticmethod
    @task.command('bankcapital')
    @click.pass_context
    def bankcapital(ctx: Context) -> None:

        bankcapital = Bankcapital(ctx.obj)
        bankcapital.main()
        ...

    @staticmethod
    @task.command('anz')
    @click.pass_context
    def anz(ctx: Context) -> None:

        anz = Anz(ctx.obj)
        anz.main()
        ...

    @staticmethod
    @task.command('aladinbank')
    @click.pass_context
    def aladinbank(ctx: Context) -> None:

        aladinbank = Aladinbank(ctx.obj)
        aladinbank.main()
        ...

    @staticmethod
    @task.command('ctbcbank')
    @click.pass_context
    def ctbcbank(ctx: Context) -> None:
        
        ctbcbank = Ctbcbank(ctx.obj)
        ctbcbank.main()
        
        ...
        
    @staticmethod
    @task.command('commbank')
    @click.pass_context
    def commbank(ctx: Context) -> None:

        commbank = Commbank(ctx.obj)
        asyncio.run(commbank.main())
        ...
        
    @staticmethod
    @task.command('btpn')
    @click.pass_context
    def btpn(ctx: Context) -> None:
        
        btpn = Btpn(ctx.obj)
        btpn.main()
        
        ...
        
    @staticmethod
    @task.command('bankvictoriasyariah')
    @click.pass_context
    def bankvictoriasyariah(ctx: Context) -> None:
        
        bankvictoriasyariah = Bankvictoriasyariah(ctx.obj)
        bankvictoriasyariah.main()
        
        ...
        
    @staticmethod
    @task.command('krom')
    @click.pass_context
    def krom(ctx: Context) -> None:
        
        krom = Krom(ctx.obj)
        krom.main()
        
        ...
        
    @staticmethod
    @task.command('bjj')
    @click.pass_context
    def bjj(ctx: Context) -> None:
        
        bjj = Bjj(ctx.obj)
        bjj.main()
        
        ...
        
    @staticmethod
    @task.command('bankneocommerce')
    @click.option('--headless', '-h', is_flag=True, default=False)
    @click.pass_context
    def bankneocommerce(ctx: Context, **kwargs) -> None:
        
        bankneocommerce = Bankneocommerce(ChainMap(ctx.obj, kwargs))
        bankneocommerce.main()
        
        ...
        
    @staticmethod
    @task.command('panin')
    @click.pass_context
    def panin(ctx: Context) -> None:
        
        panin = Panin(ctx.obj)
        panin.main()
        
        ...
        
    @staticmethod
    @task.command('kbbanksyariah')
    @click.pass_context
    def kbbanksyariah(ctx: Context) -> None:
        
        kbbanksyariah = Kbbanksyariah(ctx.obj)
        kbbanksyariah.main()
        
        ...
        
    @staticmethod
    @task.command('okbank')
    @click.pass_context
    def okbank(ctx: Context) -> None:
        
        okbank = Okbank(ctx.obj)
        okbank.main()
        
        ...
        
    @staticmethod
    @task.command('amarbank')
    @click.pass_context
    def amarbank(ctx: Context) -> None:
        
        amarbank = Amarbank(ctx.obj)
        amarbank.main()
        
        ...
        
    @staticmethod
    @task.command('seabank')
    @click.pass_context
    def seabank(ctx: Context) -> None:
        
        seabank = Seabank(ctx.obj)
        seabank.main()
        
        ...
        
    @staticmethod
    @task.command('bcasyariah')
    @click.pass_context
    def bcasyariah(ctx: Context) -> None:
        
        bcasyariah = Bcasyariah(ctx.obj)
        bcasyariah.main()
        
        ...
        
    @staticmethod
    @task.command('jago')
    @click.pass_context
    def jago(ctx: Context) -> None:
        
        jago = Jago(ctx.obj)
        jago.main()
        
        ...
        
    @staticmethod
    @task.command('bankmas')
    @click.pass_context
    def bankmas(ctx: Context) -> None:
        
        bankmas = Bankmas(ctx.obj)
        bankmas.main()
        
        ...
        
    @staticmethod
    @task.command('superbank')
    @click.pass_context
    def superbank(ctx: Context) -> None:
        
        superbank = Superbank(ctx.obj)
        superbank.main()
        
        ...
        
    @staticmethod
    @task.command('bankmandiritaspen')
    @click.pass_context
    def bankmandiritaspen(ctx: Context) -> None:
        
        bankmandiritaspen = Bankmandiritaspen(ctx.obj)
        bankmandiritaspen.main()
        
        ...
        
    @staticmethod
    @task.command('victoriabank')
    @click.pass_context
    def victoriabank(ctx: Context) -> None:
        
        victoriabank = Victoriabank(ctx.obj)
        victoriabank.main()
        
        ...