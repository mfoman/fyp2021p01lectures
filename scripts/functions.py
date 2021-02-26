def barplot(data, field_name, field_categories):
	"""Make a bar plot of a categorical variable, given as a field field_name in the
	structured array data. Field categories and their names are given in the dict field_categories.
	"""

	categories, counts = np.unique(data[field_name], return_counts=True)

	fig = plt.figure(figsize=(4, 3))
	axes = fig.add_axes([0, 0, 1, 1]) # left, bottom, width, height (range 0 to 1)
	axes.bar(range(len(categories)), counts, fc="gray") # fc is the face color

	axes.set_xlabel("")
	axes.set_ylabel('Count')
	axes.set_title(field_name)
	fig.autofmt_xdate(rotation=45)

	axes.set_xticks(range(len(categories)))
	axes.set_xticklabels([field_categories[c] for c in categories]);

def get_pearson_test(observed):
    
    rowTotals = observed.sum(axis = 1) # R
    N = rowTotals.sum()
    
    chiVal, pVal, df, expected = chi2_contingency(observed)
    
    V = np.sqrt( (chiVal/N) / (min(observed.shape)-1) )

    return chiVal, pVal, df, observed, expected, V

def plot_pearson_test(observed, expected, title, var1_labels=None, var2_labels=None):
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 6))

    severity_labels = var2_labels
    #speed_categories = {20: "20 MPH", 30: "30 MPH", 40: "40 MPH", 50: "50 MPH", 60: "60 MPH", 70: "70 MPH"}
    
    x = np.array(list(var1_labels.keys()))

    for i, ax in enumerate(axes[0]):
        ax.plot(x, observed[:,i], 'ro-', label='Observed')
        ax.plot(x, expected[:,i], 'bo-', label='Expected')
        if i==0: 
            ax.set_ylabel('Casualties')
            ax.legend(loc='best');
        ax.set_title(severity_labels[i])
        ax.set_xticks(x)
        ax.set_xticklabels(list(var1_labels.values()))
        fig.autofmt_xdate(rotation=45)

    for i, ax in enumerate(axes[1]):
        ax.plot(x, observed[:,i]/expected[:,i], 'go-')
        ax.plot(x, np.ones(x.shape), 'k:')
            
        ax.plot(x, np.ones(x.shape)/2, 'm:', label='Significance level')
        
        if i==0: 
            ax.legend(loc='best');

        if i==0: 
            ax.set_ylabel('Observed/Expected')
        ax.set_xticks(x)
        ax.set_xticklabels(list(var1_labels.values()))
        fig.autofmt_xdate(rotation=45)
    
    fig.suptitle(title)
    
print("Loaded functions.\n")