import json

import click

from vpfq.SampleDataParamType import SampleDataParamType
from vpfq.VpfqPolicy import VpfqPolicy


@click.group()
def cli():
    pass


@cli.command(context_settings=dict(max_content_width=500))
@click.argument('output_file', type=click.File('w'))
@click.option('--segments', '-s', type=click.IntRange(2, 4998), default=20, help="Number of segments", required=False)
@click.option('--sample-data', '-d', type=SampleDataParamType(), default="(0,0), (1,0.1), (2,2), (4,6), (7,20), (9,50), (10,100)", help="Input data for interpolation", required=False)
@click.option("--cookie-name", "-c", help="VPFQ cookie name (akavpfq_<VP-instance-label>)", required=True)
@click.option("--queue-endpoint", "-e", default="/__queue", help="VPFQ queue endpoint)", required=False)
@click.option("--target-probability", "-t", default=100, help="Target probability 0-100 (float numbers)", type=click.FloatRange(0, 100), required=False)
def generate_policy(output_file, segments, sample_data, cookie_name, queue_endpoint, target_probability):
    """ Generate VPFQ policy """
    policy = VpfqPolicy(queue_endpoint, cookie_name)
    json.dump(policy.generate_json(sample_data[0], sample_data[1], segments, target_probability), output_file)


if __name__ == '__main__':
    cli(obj={})
