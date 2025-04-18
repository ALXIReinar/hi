""" вспомогательный код для модульных тестов """
import pytest
from src.event_types import Event

from src.config import COMMUNICATION_GATEWAY_QUEUE_NAME, \
    LOG_DEBUG, LOG_INFO
from src.config import CONTROL_SYSTEM_QUEUE_NAME
from src.queues_dir import QueuesDirectory
from src.security_monitory import BaseSecurityMonitor
from src.security_policy_type import SecurityPolicy


@pytest.fixture(scope="module")
def queues_dir() -> QueuesDirectory:
    """ каталог очередей """
    return QueuesDirectory()


class SecurityMonitor(BaseSecurityMonitor):
    """ класс монитора безопасности """

    def __init__(self, queues_dir):
        super().__init__(queues_dir)
        self._init_set_security_policies()

    def _init_set_security_policies(self):
        """ инициализация политик безопасности """
        default_policies = [
            SecurityPolicy(
                source=COMMUNICATION_GATEWAY_QUEUE_NAME,
                destination=CONTROL_SYSTEM_QUEUE_NAME,
                operation='set_mission')
        ]
        self.set_security_policies(policies=default_policies)

    def set_security_policies(self, policies):
        """ установка новых политик безопасности """
        self._security_policies = policies
        self._log_message(
            LOG_INFO, f"изменение политик безопасности: {policies}")

    def _check_event(self, event: Event):
        """ проверка входящих событий """
        self._log_message(
            LOG_DEBUG, f"проверка события {event}, по умолчанию выполнение запрещено")

        authorized = False
        request = SecurityPolicy(
            source=event.source,
            destination=event.destination,
            operation=event.operation)

        if request in self._security_policies:
            self._log_message(
                LOG_DEBUG, "событие разрешено политиками, выполняем")
            authorized = True

        return authorized

@pytest.fixture
def security_monitor(queues_dir) -> SecurityMonitor:
    """ монитор безопасности """
    sm = SecurityMonitor(queues_dir=queues_dir)
    sm.log_level = LOG_DEBUG
    assert sm is not None
    return sm

QGC WPL 110
0	1	0	16	0	5	0	0	55.781529  49.116457	0	1

1	0	3	16	0	5	0	0	55.781584  49.116600	0	1
2	0	3	16	0	5	0	0	55.781741  49.116515	0	1
3	0	3	16	0	5	0	0	55.782206  49.115948	0	1
4	0	3	16	0	5	0	0	55.782670  49.116050	0	1
5	0	3	16	0	5	0	0	55.784517  49.118530	0	1

6	0	3	16	0	5	0	0	55.784580  49.119314	0	1

7	0	3	16	0	5	0	0	55.782228  49.123323	0	1
8	0	3	16	0	5	0	0	55.781794  49.123832	0	1

9	0	3	16	0	5	0	0	55.778965  49.126659	0	1

10	0	3	16	0	5	0	0	55.778442  49.127369	0	1

11	0	3	16	0	5	0	0	55.773324  49.139169	0	1
12	0	3	16	0	5	0	0	55.771971  49.141849	0	1
13	0	3	16	0	5	0	0	55.768973  49.145400	0	1

14	0	3	16	0	5	0	0	55.764580  49.149288	0	1
15	0	3	16	0	5	0	0	55.763801  49.149814	0	1
16	0	3	16	0	5	0	0	55.759727  49.153640	0	1






17	0	3	16	0	5	0	0	55.752973  49.162104	0	1
18	0	3	16	0	5	0	0	55.752394  49.162584	0	1
19	0	3	16	0	5	0	0	55.752128  49.162868	0	1
20  0	3	16	0	5	0	0	55.751670  49.163343	0	1
21	0	3	16	0	5	0	0	55.751582  49.164018	0	1
22	0	3	16	0	5	0	0	55.751762  49.164564	0	1
23	0	3	16	0	5	0	0	55.752669  49.166577    0  	1
24	0	3	16	0	5	0	0	55.753053  49.168840	0	1
25	0	3	16	0	5	0	0	55.755565  49.172623	0	1
26	0	3	16	0	5	0	0	55.756363  49.174638	0	1
27	0	3	16	0	5	0	0	55.757316  49.181633	0	1
28	0	3	16	0	5	0	0	55.757650  49.182567	0	1
29	0	3	16	0	5	0	0	55.759709  49.185319	0	1
30	0	3	16	0	5	0	0	55.760101  49.186330	0	1
31	0	3	16	0	5	0	0	55.760488  49.188577	0	1

32	0	3	16	0	5	0	0	55.760937  49.189504    0	1

33	0	3	16	0	5	0	0	55.760749  49.190122    0	1
34	0	3	16	0	5	0	0	55.752983  49.203538    0	1
35	0	3	16	0	5	0	0	55.752496  49.204378    0	1
36	0	3	16	0	5	0	0	55.748301  49.211524    0	1

37	0	3	16	0	5	0	0	55.748005  49.211900    0	1
38	0	3	16	0	5	0	0	55.747492  49.212791    0	1
39	0	3	16	0	5	0	0	55.747332  49.212512    0	1
40	0	3	16	0	5	0	0	55.747332  49.212512    0	1


41	0	3	16	0	5	0	0	55.747894  49.211070    0	1
42	0	3	16	0	5	0	0	55.747422  49.210193    0	1
43	0	3	16	0	5	0	0	55.747672  49.209927    0	1

