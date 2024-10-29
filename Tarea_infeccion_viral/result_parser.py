import pandas as pd

data = pd.read_csv("b.csv", header=None).transpose()

data.columns = data.iloc[0]
data = data.drop(0)

data["immunization-coverage"] = data["immunization-coverage"].astype(float)
data["[total_steps]"] = data["[total_steps]"].astype(float)

metrics = {}

immunization_types = ['hubs', 'random']
coverages = [0.25, 0.5, 0.75, 0.9]

for immun_type in immunization_types:
    for coverage in coverages:
        subset = data[(data["immuniaztion-type"] == immun_type) & (data["immunization-coverage"] == coverage)]
        
        if not subset.empty:
            total_steps = subset["[total_steps]"]
            metrics[(immun_type, coverage)] = {
                'Immunization Type': immun_type,
                'Coverage': coverage,
                'Mean': total_steps.mean(),
                'Median': total_steps.median(),
                'Standard Deviation': total_steps.std(),
                'Min': total_steps.min(),
                'Max': total_steps.max()
            }


metrics_df = pd.DataFrame.from_dict(metrics, orient='index')

metrics_df.to_csv("metrics_output_b.csv", index=False)

print("Metrics saved to 'metrics_output.csv'")
