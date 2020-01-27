import logging
import json

logger = logging.getLogger(__name__)


def process_scout_suite_telemetry(collector_results, monkey_guid):
    # Monkey.get_single_monkey_by_guid(monkey_guid).set_hostname(collector_results["hostname"])
    logger.info(f"\n\n{json.dumps(collector_results, indent=2)}\n{monkey_guid}")