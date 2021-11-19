import matplotlib.pyplot as plt

def plot_loss(losses, params, loss_type, set_type='', prepr_type=''):
    plt.plot(list(range(params['n_epochs'])), losses)

    plt.ylabel("mse loss")
    plt.xlabel("epochs")

    params_to_string = "E{0}_HS{1}_NL_{2}_BS_{3}_LR{4}_G{5}_DROP{6}".format(
        params['n_epochs'],
        params['hs'],
        params['n_layers'],
        params['b_size'],
        str(params['l_rate']).replace('.', '_'),
        str(params['gamma']).replace('.', '_'),
        str(params['dropout']).replace('.', '_'))

    plt.title(f"{params_to_string} training {loss_type}")

    save(f"./plots/{set_type}_{prepr_type}_losses_{params_to_string}_.png")

def save(title):
    plt.savefig(title)
    plt.clf()