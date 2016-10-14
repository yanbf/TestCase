import datetime
import random
from model import *
DB11_master = create_engine(
    DB_STR_11, pool_recycle=3600, pool_size=50, poolclass=pool.SingletonThreadPool)
get_db11_master_cursor = get_cursor_factory(DB11_master)

class FakeReport:
    '''
    log_time: confined to month
    '''
    FIELDS = [
        'log_time',
        'pmd_account_id',
        'pmd_campaign_id',
        'pmd_offer_id',
        'pmd_offer_type',
        'pmd_adset_id',
        'pmd_ad_id',
        'fb_ad_account_id',
        'fb_campaign_id',
        'fb_adset_id',
        'fb_ad_id',
        'fb_clicks',
        'fb_impressions',
        'fb_conversions',
        'fb_cost',
        'fb_revenue',
        'view_content',
        'add_to_cart',
        'add_to_wishlist',
        'initiate_checkout',
        'add_payment_info',
        'complete_registration',
        'purchase',
        'search',
        'lead',
        'purchase_revenue',
        'lead_revenue'
    ]

    FB_ID_LINKS = [
        # pmd_campaign_id, pmd_adset_id, pmd_ad_id, fb_ad_account_id, fb_campaign_id, fb_adset_id, fb_ad_id
		("5883", "50670", "53581", "act_858751837556226", "6057315263252", "6057315265052", "6057315273852"),
		("5883", "50671", "53582", "act_858751837556226", "6057315263252", "6057315266052", "6057315274652"),
		("5883", "50672", "53583", "act_858751837556226", "6057315263252", "6057315264252", "6057315273452"),
		("5884", "50675", "53584", "act_858751837556226", "6057315382452", "6057315484452", "6057315488652"),
		("5887", "50681", "53594", "act_858751837556226", "6057316459652", "6057316460852", "6057316465052"),
		("5886", "50680", "53591", "act_858751837556226", "6057316408252", "6057316409052", "6057316416452"),
		("5886", "50680", "53592", "act_858751837556226", "6057316408252", "6057316409052", "6057316416652"),
		("5886", "50680", "53593", "act_858751837556226", "6057316408252", "6057316409052", "6057316411852"),
		("5912", "50694", "53608", "act_858751837556226", "6057329963052", "6057330093452", "6057330106652"),
		("5912", "50694", "53609", "act_858751837556226", "6057329963052", "6057330093452", "6057330107052"),
		("5912", "50695", "53610", "act_858751837556226", "6057329963052", "6057330093652", "6057330106852"),
		("5912", "50695", "53611", "act_858751837556226", "6057329963052", "6057330093652", "6057330107852"),
		("5912", "50696", "53612", "act_858751837556226", "6057329963052", "6057330093252", "6057330106452"),
		("5912", "50696", "53613", "act_858751837556226", "6057329963052", "6057330093252", "6057330115852"),
		("5915", "50706", "53623", "act_858751837556226", "6057334805852", "6057334808052", "6057334829852"),
		("5915", "50705", "53622", "act_858751837556226", "6057334805852", "6057334807052", "6057334830452"),

    ]

    MAX_CONVERSIONS = 50
    MAX_CLICKS = 100
    MAX_IMPRESSIONS = 100000

    def __init__(self, *args, **kwargs):
        self._formater = \
            ", ".join(["%s" for _ in range(7)]) + \
            ", \"%s\", \"%s\", \"%s\", \"%s\", " + \
            ", ".join(["%s" for _ in range(16)])
        # for time
        now = datetime.datetime.now()
        year = kwargs.get('year', now.year)
        month = int(kwargs.get('month', 0)) or random.randint(1, 7)
        day = int(kwargs.get('day', 0)) or random.randint(1, 30)

        self._log_time = "%s-%s-%s" % (
            year,
            "%02d" % month,
            "%-2d" % day
        )
        # for data
        self._conversions = random.randint(0, FakeReport.MAX_CONVERSIONS)
        self._clicks = random.randint(self._conversions, FakeReport.MAX_CLICKS)
        self._impressoins = random.randint(self._clicks, FakeReport.MAX_IMPRESSIONS)
        self._fb_cost = self._impressoins / 10 * random.random()
        self._fb_revenue = self._conversions * random.uniform(10, 20) * 100

        # for relationship
        self._account_id = kwargs.get('pmd_account_id', 0)
        relation = random.choice(FakeReport.FB_ID_LINKS)
        self._campaign_id = relation[0]
        self._adset_id = relation[1]
        self._ad_id = relation[2]
        self._adaccount_id = relation[3]
        self._fb_campaign_id = relation[4]
        self._fb_adset_id = relation[5]
        self._fb_ad_id = relation[6]

    def insert_fake_data(
        self,
        pmd_account_id=5,
        pmd_offer_id=850,
        pmd_offer_type=0,
        view_content=0,
        add_to_cart=0,
        add_to_wishlist=0,
        initiate_checkout=0,
        add_payment_info=0,
        complete_registration=0,
        purchase=0,
        search=0,
        lead=0,
        purchase_revenue=180.00,
        lead_revenue=0.0
    ):
        pmd_account_id = pmd_account_id \
            if not self._account_id else self._account_id

        data = ("(" + self._formater + ")") % (
            self._log_time,
            pmd_account_id,
            self._campaign_id,
            pmd_offer_id,
            pmd_offer_type,
            self._adset_id,
            self._ad_id,
            self._adaccount_id,
            self._fb_campaign_id,
            self._fb_adset_id,
            self._fb_ad_id,
            self._clicks,
            self._impressoins,
            self._conversions,
            self._fb_cost,
            self._fb_revenue,
            view_content,
            add_to_cart,
            add_to_wishlist,
            initiate_checkout,
            add_payment_info,
            complete_registration,
            purchase,
            search,
            lead,
            purchase_revenue,
            lead_revenue
        )

        sql_string = '''
            INSERT INTO efmp_report_data VALUES %s
        ''' % data

        print sql_string
        try:
            with get_db11_master_cursor() as cursor:
                cursor.execute(sql_string)
        except Exception, e:
            print e

        print 'insert one item'


def main():
    now = datetime.datetime.now()
    data = FakeReport(
        year=now.year,
        month='07',
        # day=now.day
    )

    data.insert_fake_data()

if '__name__' == '__main__':
    main()
