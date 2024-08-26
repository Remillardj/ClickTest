import boto3
import click

@click.command()
@click.argument('instance_id')
def stop_instance(instance_id):
    """Shuts down an EC2 instance given its instance ID."""
    ec2 = boto3.client('ec2')

    try:
        # Stop the instance
        response = ec2.stop_instances(InstanceIds=[instance_id])
        current_state = response['StoppingInstances'][0]['CurrentState']['Name']
        click.echo(f"Instance {instance_id} is now {current_state}.")
    except Exception as e:
        click.echo(f"Failed to stop instance {instance_id}: {e}")

if __name__ == '__main__':
    stop_instance()
