import pandas


def price_predictor(a_hat, b_hat, property_age):
    return a_hat + (b_hat * property_age)



df = pandas.read_csv("RiyadhVillasAqar.csv", dtype={"apartments": "str"})
df = df[["propertyAge", "square price"]]
df = df[df["propertyAge"] > 0]              #most are 0 which i think is default for NAN so getting rid of them

pAge_mean = df["propertyAge"].mean()
squarePrice_mean = df["square price"].mean()

covariance_numerator = ((df["propertyAge"] - pAge_mean) * (df["square price"] - squarePrice_mean)).sum()
sum_of_squared_deviations = ((df["propertyAge"] - pAge_mean) ** 2).sum()

b_hat = covariance_numerator // sum_of_squared_deviations
a_hat = squarePrice_mean - (b_hat * pAge_mean)


test_age = 2

print(price_predictor(a_hat, b_hat, test_age))