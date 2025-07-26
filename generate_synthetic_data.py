import pandas as pd
import random
import uuid
from datetime import datetime, timedelta
import argparse

# Helper function to generate a random timestamp within the last 30 days
def random_time():
    now = datetime.now()
    days_ago = random.randint(0, 30)
    return now - timedelta(days=days_ago, hours=random.randint(0, 23), minutes=random.randint(0, 59))

def generate_data(num_records=3000, output_file="synthetic_mule_transactions.csv"):
    accounts = [f"A{str(i).zfill(5)}" for i in range(100)]
    data = []

    for _ in range(num_records):
        sender = random.choice(accounts)
        receiver = random.choice([acc for acc in accounts if acc != sender])
        txn_amount = round(random.uniform(100, 100000), 2)
        txn_time = random_time()
        txn_type = random.choice(["transfer", "withdrawal", "deposit"])
        channel = random.choice(["mobile_app", "ATM", "branch"])
        location = random.choice(["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai"])

        txn_freq = random.randint(1, 10)
        receiver_count = random.randint(1, 5)
        same_day_txns = random.randint(0, 3)
        avg_amt = round(random.uniform(1000, 50000), 2)

        # Base fraud probability based on suspicious patterns
        fraud_score = 0
        if txn_amount > 80000:
            fraud_score += 0.4
        if txn_freq > 8:
            fraud_score += 0.3
        if same_day_txns > 2:
            fraud_score += 0.3
        if avg_amt < 2000 and txn_amount > 50000:
            fraud_score += 0.2
        if receiver_count > 3:
            fraud_score += 0.2

        # Cap fraud_score at 1.0
        fraud_score = min(fraud_score, 1.0)

        # Probabilistic labeling
        is_fraud = 1 if random.random() < fraud_score else 0

        data.append({
            "transaction_id": str(uuid.uuid4()),
            "sender_account_id": sender,
            "receiver_account_id": receiver,
            "transaction_amount": txn_amount,
            "transaction_time": txn_time.strftime("%Y-%m-%d %H:%M:%S"),
            "transaction_type": txn_type,
            "channel": channel,
            "location": location,
            "transaction_frequency": txn_freq,
            "receiver_count": receiver_count,
            "same_day_repeat_txns": same_day_txns,
            "avg_transaction_amount": avg_amt,
            "is_flagged_fraud": is_fraud
        })

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"✅ Synthetic dataset with {num_records} transactions saved to '{output_file}'.")

# CLI entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=3000, help="Number of transactions to generate")
    parser.add_argument("--o", type=str, default="synthetic_mule_transactions.csv", help="Output CSV filename")
    args = parser.parse_args()

    generate_data(num_records=args.n, output_file=args.o)