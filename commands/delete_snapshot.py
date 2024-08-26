import boto3
import click

@click.command()
@click.argument('snapshot_id')
def delete_snapshot(snapshot_id):
    """Deletes an AWS snapshot given its snapshot ID."""
    ec2 = boto3.client('ec2')

    try:
        # Delete the snapshot
        response = ec2.delete_snapshot(SnapshotId=snapshot_id)
        click.echo(f"Snapshot {snapshot_id} deleted successfully.")
    except Exception as e:
        click.echo(f"Failed to delete snapshot {snapshot_id}: {e}")

if __name__ == '__main__':
    delete_snapshot()
