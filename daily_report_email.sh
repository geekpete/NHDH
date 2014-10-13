#!/bin/bash
curl http://localhost:5000/fetch
curl http://localhost:5000/mail/314291494078-aws-billing-detailed-line-items-with-resources-and-tags-`date +"%Y"`-`date +"%m"`.csv
