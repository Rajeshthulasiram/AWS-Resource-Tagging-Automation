
---

### **📌 `eventbridge_rule.md` (EventBridge Setup)**
```md
# AWS EventBridge Rule for Automated Tagging

## **🎯 Goal**
Schedule **Lambda Function Execution** every **6 hours** to keep AWS resources tagged.

## **🔹 Steps**
1. Open **AWS EventBridge Console**.
2. Click **Create Rule**.
3. **Rule Name**: `Auto-Tag-Resources`
4. **Define Pattern** → Select **Schedule**.
5. Choose **Rate expression**:

**rate(6 hours)**

6. **Target** → Select **AWS Lambda**.
7. Choose **Lambda Function**: `Auto-Tag-Resources`.
8. Click **Create Rule**.

✅ Now, your tagging function runs **every 6 hours** automatically!
