"""Module for lambda to process data."""
import datetime
import sqlalchemy as sq
import boto3


def lambda_handler(event=None, context=None):
    """Handle lamba calls."""
    fnames = get_filenames()
    dates = get_timestamps()
    deleted_files = []

    for fname in fnames:
        if datetime.datetime.strptime(fname[:-4], "%Y%m%d-%H%M") in dates:
            deleted_files.append(delete_file(fname))

    return deleted_files


def delete_file(fname):
    """Delete file in given path."""
    s3_client = boto3.client(
        "s3",
        aws_access_key_id="XXXX",
        aws_secret_access_key="XXX",
        region_name="us-west-1",
    )
    s3_client.delete_object(Bucket="gbfs-data", Key=fname)
    return fname


def get_filenames():
    """Get all the filenames in the bucket."""
    tab = []
    s3_client = boto3.client(
        "s3",
        aws_access_key_id="****",
        aws_secret_access_key="****",
        region_name="us-west-1",
    )

    dd = s3_client.list_objects_v2(Bucket="gbfs-data")

    for key in dd["Contents"]:
        tab.append(key["Key"])

    return tab


def get_timestamps():
    """Get timestamps."""
    engine = sq.create_engine(
        "{}://{}:{}@gbfs-data.cocxlae2ptlp.us-west-1.rds.amazonaws.com/{}".format(
            "postgresql", "stations_data", "gbfs_db_admin", "PASSWORD"
        )
    )
    with engine.connect() as conn:
        cmd = "SELECT DISTINCT timestamp FROM public.stations_status" "ORDER BY timestamp ASC;"
        rs = conn.execute(cmd)  # type: ignore

    tab = []
    for row in rs:
        tab.append(row[0])

    return tab


if __name__ == "__main__":
    print(lambda_handler())
