#!/usr/bin/env python

from constructs import Construct
from cdktf import App, TerraformStack

from imports.aws import AwsProvider
from imports.aws import SecurityGroup, SecurityGroupIngress


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        region = 'us-east-1'
        AwsProvider(self, 'Aws', region=region)

        allow = SecurityGroupIngress(
            cidr_blocks=['8.8.8.8/32'],
            ipv6_cidr_blocks=[],
            protocol='tcp',
            from_port=5432,
            to_port=5432,
            description="Allow",
            prefix_list_ids=[],
            security_groups=[],
            self_attribute=False
        )

        sec_group_name = 'cdktf-sg-test'
        vpc_id = 'your-vpc-id'
        SecurityGroup(
            self, sec_group_name, vpc_id=vpc_id,
            ingress=[allow]
        )


app = App()
MyStack(app, "terraform-cdk-sgbug")

app.synth()
