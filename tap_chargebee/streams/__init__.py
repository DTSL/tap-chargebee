from .addons import AddonsStream
from .coupons import CouponsStream
from .credit_notes import CreditNotesStream
from .customers import CustomersStream
from .events import EventsStream
from .invoices import InvoicesStream
from .payment_sources import PaymentSourcesStream
from .plans import PlansStream
from .subscriptions import SubscriptionsStream
from .transactions import TransactionsStream
from .transactions_without_update import TransactionsWithoutUpdateStream
from .virtual_bank_accounts import VirtualBankAccountsStream
from .credit_notes import CreditNotesStream
from .gifts import GiftsStream
from .orders import OrdersStream
from .promotional_credits import PromotionalCreditsStream
from .item_prices import ItemPricesStream
from .items import ItemsStream
from .unbilled_charges import UnbilledCharges

AVAILABLE_STREAMS = [
    EventsStream,
    CouponsStream,
    CreditNotesStream,
    CustomersStream,
    GiftsStream,
    InvoicesStream,
    OrdersStream,
    PaymentSourcesStream,
    PromotionalCreditsStream,
    SubscriptionsStream,
    TransactionsStream,
    TransactionsWithoutUpdateStream,
    VirtualBankAccountsStream,
    UnbilledCharges
]

AVAILABLE_STREAMS_1_0_ONLY = [
    AddonsStream,
    PlansStream
]

AVAILABLE_STREAMS_2_0_ONLY = [
    ItemsStream,
    ItemPricesStream
]

AVAILABLE_STREAMS_1_0 = AVAILABLE_STREAMS + AVAILABLE_STREAMS_1_0_ONLY

AVAILABLE_STREAMS_2_0 = AVAILABLE_STREAMS + AVAILABLE_STREAMS_2_0_ONLY

AVAILABLE_STREAMS_ALL = AVAILABLE_STREAMS + AVAILABLE_STREAMS_1_0_ONLY + AVAILABLE_STREAMS_2_0_ONLY