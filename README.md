# VP policy generator

This CLI generates Visitor Prioritization policy.

Features:

* linear interpolation based on input data
* variable number of segments
* JSON and CSV outputs

## Usage

```
Usage: vpfq generate-policy [OPTIONS] OUTPUT_FILE

  Generate VPFQ policy

Options:
  --output-format [JSON|CSV]      [default: JSON]
  -s, --segments INTEGER RANGE    Number of segments  [default: 20]
  -d, --sample-data SAMPLE-DATA   Input data for interpolation  [default: (0,0), (1,0.1), (2,2), (4,6), (7,20), (9,50), (10,100)]
  -c, --cookie-name TEXT          VPFQ cookie name (akavpfq_<VP-instance-label>)  [required]
  -e, --queue-endpoint TEXT       VPFQ queue endpoint)  [default: /__queue]
  -t, --target-probability FLOAT RANGE
                                  Target probability 0-100 (float numbers)  [default: 100]
  --help                          Show this message and exit.
```

Example execution:

```
vpfq generate-policy -s 100 -c akavpfq_test output.json
```

The file created by the CLI can be deployed to Akamai using OPEN API directly:

```
http --timeout=120 -a SECTION: --auth-type edgegrid PUT ':/cloudlets/api/v2/policies/POLICY_ID/versions/VERSION' @output.json
```

> Don't forget to replace _SECTION_, _POLICY_ID_ and _VERSION_ in the above command to respective values in your environment.


or by using Cloudlet CLI:

```
akamai cloudlets update --policy-id 12345 --file output.json
...searching for cloudlet policy-id 12345
...found policy-id 12345
Updating policy mypolicy
28
```

### Sample data

Sample data should be provided as list of tuples (x,y), ie:

```
(0,0), (1,0.1), (2,2), (4,6), (7,20), (9,50), (10,100)
```

The data is used for interpolation algorithm to adjust probability function to given number of segments.

### Using Docker image

```
docker run --rm -it lukaszczerpak/vpf-cli vpfq generate-policy -c akavpfq_test - > output.json
```
