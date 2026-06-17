# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vaivtpuran 17.1094)
- **Original**: हैं। कभी रासमण्डलमें विराजमान हो राधा-
- **Translation**: 

---

### Verse 2 (Vaivtpuran 17.1095)
- **Original**: + ब्रहमखण्ड + कई 55% %$ 454 $ 5 $ 5 5 $ ऊ $ $ $ $ $ $ $ 88 4458 # 5 56 # 58% # 68668 68 5
- **Translation**: 

---

### Verse 3 (Vaivtpuran 17.1096)
- **Original**: # 664 &
- **Translation**: 

---

### Verse 4 (Vaivtpuran 17.1097)
- **Original**: 8 5 6 4 846 488 5
- **Translation**: 

---

### Verse 5 (Vaivtpuran 17.1098)
- **Original**: 8 8 88 6 8 88 5 / रानीसे समाराधित होते हैं। कभी गोप-बालकोंसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 17.1099)
- **Original**: अंशकलाद्वारा जगत॒की रक्षाके लिये लीलापूर्वक घिरे हुए गोपवेषसे सुशोभित होते हैं। कभी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 17.1100)
- **Original**: नाना प्रकारके अवतार धारण करते हैं। उन सैकड़ों शिखरबाले गिरिराज गोवर्धनके कारण
- **Translation**: 

---

### Verse 8 (Vaivtpuran 17.1101)
- **Original**: अवतारोंके बे स्वयं ही सनातन बीज हैं। कभी उत्कृष्ट शोभासे युक्त रमणीय बृन्दाबनमें कामधेनुओंके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 17.1102)
- **Original**: योगियों एबं संत-महात्माओंके हृदयमें निवास समुदायको चराते हुए बालगोपालके रूपमें देखे करते हैं। बे ही प्राणियोंके प्राणस्वरूप परमात्मा जाते हैं। कभी गोलोकमें विरजाके तटपर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 17.1103)
- **Original**: एवं परमेश्वर हैं। मैं मूढ़ अबला उन निर्गुण एवं पारिजातबनमें मधुर-मधुर बेणु बजाकर गोपाडुनाओंको
- **Translation**: 

---

### Verse 11 (Vaivtpuran 17.1104)
- **Original**: सर्वव्यापी भगवान्‌की स्तुति करनेमें सर्वथा मोहित किया करते हैं। कभी निरामय वैकुण्ठधाममें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 17.1105)
- **Original**: असमर्थ हूँ। वे अलक्ष्य, अनीह, सारभूत तथा चतुर्भुज लक्ष्मीकान्तके रूपमें रहकर चार भुजाधारी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 17.1106)
- **Original**: मन और वाणीसे परे हैं। भगवान्‌ अनन्त सहस्र पार्षदोंसे सेवित होते हैं। कभी तीनों लोकोंके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 17.1107)
- **Original**: मुखोंद्वार भी उनकी स्तुति नहीं कर सकते। कद अपने अंशरूपसे श्वेतट्वीपमें विष्णुरूप
- **Translation**: 

---

### Verse 15 (Vaivtpuran 17.1108)
- **Original**: पश्ममुख महादेव, चतुर्मुख ब्रह्मा, गजानन गणेश धारण करके रहते हैं और पद्मा उनकी सेवा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 17.1109)
- **Original**: और षडानन कार्तिकेय भी जिनकी स्तुति करनेमें करती हैं। कभी किसी ब्रह्माण्डमें अपनी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 17.1110)
- **Original**: समर्थ नहीं हैं, माया भी जिनकी मायासे मोहित अंशकलाद्दारा ब्रह्मारूपसे विराजमान होते हैं।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 17.1111)
- **Original**: रहती है, लक्ष्मी भी जिनकी स्तुति करनेमें सफल कभी अपने ही अंशसे कल्याणदायक मड्जलरूप
- **Translation**: 

---

### Verse 19 (Vaivtpuran 17.1112)
- **Original**: नहीं होती, सरस्वती भी जडबवत्‌ हो जाती है शिव-विग्रह धारण करके शिवधाममें निवास
- **Translation**: 

---

### Verse 20 (Vaivtpuran 17.1113)
- **Original**: और वेद भी जिनका स्तवन करनेमें अपनी शक्ति करते हैं। अपने सोलहवें अंशसे स्वयं ही
- **Translation**: 

---

