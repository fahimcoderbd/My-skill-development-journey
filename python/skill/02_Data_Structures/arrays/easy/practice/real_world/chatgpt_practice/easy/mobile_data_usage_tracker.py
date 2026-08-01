'''
চলো, এবার একটা **একদম beginner-friendly real-world Array problem** দিই। Solution দেখবে না, নিজে solve করার চেষ্টা করো।

# 📱 Mobile Data Usage Tracker

তোমার গত ৭ দিনের mobile data usage (MB-তে):

```python
data_usage = [500, 750, 300, 1200, 450, 800, 600]
```

## Tasks

1. মোট কত MB data ব্যবহার হয়েছে?
2. সবচেয়ে বেশি data কোন দিনে ব্যবহার হয়েছে? (শুধু value বের করো)
3. সবচেয়ে কম data কোন দিনে ব্যবহার হয়েছে? (শুধু value বের করো)
4. কতদিন 700 MB-এর বেশি data ব্যবহার হয়েছে?
5. Average data usage কত?

---

### Expected Output Format

```text
Total Data Used: ?
Highest Usage: ?
Lowest Usage: ?
Days Above 700 MB: ?
Average Usage: ?
```

---

### Bonus Challenge 🚀

Loop ব্যবহার করে বের করো:

```python
data_usage = [500, 750, 300, 1200, 450, 800, 600]
```

প্রথমবার `1000 MB`-এর বেশি usage কোথায় হয়েছে? (index বের করো)

'''

def get_average(total,length):
    return total / length

def data_usage_tracker(arr):
    if not arr:
        return None
    
    total_data_usage = sum(arr)
    highest_data_day = arr.index(max(arr)) + 1
    minimum_data_day = arr.index(min(arr)) + 1
    data_more_than_700mb = 0

    for data in arr:
        if data > 700:
           data_more_than_700mb += 1

    return (
        f"Total Data Used: {total_data_usage} mb \n"
        f"Highest Usage:  {highest_data_day} \n"
        f"Lowest Usage: Day {minimum_data_day} \n"
        f"Days Above 700 MB: {data_more_than_700mb} days \n"
        f"Average Usage: {get_average(total_data_usage, len(arr)):.2f}"
    )

#testing
data_usage = [500, 750, 300, 1200, 450, 800, 600]
print(data_usage_tracker(data_usage))

