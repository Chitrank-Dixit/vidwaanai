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

### Verse 1 (Bramha 0.4021)
- **Original**: शक्तिदाता! आपकी जय हो, आप ही शक्ति हैं। आपको नमस्कार है। देव! आपकी जय हो, जय
- **Translation**: 

---

### Verse 2 (Bramha 0.4022)
- **Original**: विजयका वरदान देनेवाले ईश्वर! आपकी जय हो। आप विश्वका पालन और धारण करनेवाले
- **Translation**: 

---

### Verse 3 (Bramha 0.4023)
- **Original**: हो। यज्ञदाता! आपकी जय हो। आप ही यज्ञ हैं। हैं। ईश ! आपकी जय हो। आप सदसत्स्वरूप
- **Translation**: 

---

### Verse 4 (Bramha 0.4024)
- **Original**: आपके नेत्र पद्मपत्रकी तरह विशाल हैं। आपकी हैं। माधव! आपको जय हो। आप धर्मनिष्ठ
- **Translation**: 

---

### Verse 5 (Bramha 0.4025)
- **Original**: जय हो। दान देनेवाले परमेश्वर! आपकी जय हो। परमात्माको नमस्कार है। कामनाओंको पूर्ण करनेवाले
- **Translation**: 

---

### Verse 6 (Bramha 0.4026)
- **Original**: आप ही दान हैं। कैटभका नाश करनेवाले और कामस्वरूप केशव! आपकी जय हो।
- **Translation**: 

---

### Verse 7 (Bramha 0.4027)
- **Original**: नारायण! आपकी जय हो। कीर्तिदाता! आपकी गुणोंके सागर श्रीराम ! आपकी जय हो। आप
- **Translation**: 

---

### Verse 8 (Bramha 0.4028)
- **Original**: जय हो। आप ही कीर्ति हैं। मूर्तिदाता! आपकी पुष्टि देनेवाले और पुष्टिके स्वामी हैं। आपकी जय
- **Translation**: 

---

### Verse 9 (Bramha 0.4029)
- **Original**: जय हो। आप ही मूर्ति धारण करनेवाले हैं। हो, जय हो। कल्याणदाता! आपको नमस्कार है।
- **Translation**: 

---

### Verse 10 (Bramha 0.4030)
- **Original**: सौख्यदाता! आपकी जय हो। आप ही सौख्यस्वरूप सम्पूर्ण भूतोंके पालक! आपकी जय हो। भूतेश्वर !
- **Translation**: 

---

### Verse 11 (Bramha 0.4031)
- **Original**: हैं। पायनको भी पावन बनानेवाले परमात्मन्‌ ! आपकी जय हो। आप मौन धारण करनेवाले हैं।
- **Translation**: 

---

### Verse 12 (Bramha 0.4032)
- **Original**: आपकी जय हो। शान्तिदाता! आपकी जय हो! आपको नमस्कार है। कर्मफलोंके दाता! आपकी
- **Translation**: 

---

### Verse 13 (Bramha 0.4033)
- **Original**: आप ही शान्ति हैं। भगवान्‌ शंकरकी भी उत्पत्तिके जय हो। आप ही कर्मस्वरूप हैं। पीताम्बरधारी
- **Translation**: 

---

### Verse 14 (Bramha 0.4034)
- **Original**: कारण! आपकी जय हो। ज्योतिःस्वरूप! आपकी प्रभो! आपकी जय हो। सर्वेश्वर आपकी जय
- **Translation**: 

---

### Verse 15 (Bramha 0.4035)
- **Original**: जय हो। वामन! आपकी जय हो। वित्तेश! आपकी हो। आप सर्वस्वरूप हैं। आप मब़जलरूप प्रभुको
- **Translation**: 

---

### Verse 16 (Bramha 0.4036)
- **Original**: जय हो। धूममयी पताकावाले! आपकी जय हो। नमस्कार है। नाथ! आप सत्त्वगुणके अधिनायक
- **Translation**: 

---

### Verse 17 (Bramha 0.4037)
- **Original**: सम्पूर्ण जगत॒के लिये दातारूप परमेश्वर! आपको हैं। आपकी जय हो, जय हो। आप सम्पूर्ण
- **Translation**: 

---

### Verse 18 (Bramha 0.4038)
- **Original**: नमस्कार है। पुण्डरीकाक्ष! आप ही त्िलोकोीमें वेदोंके ज्ञाता हैं। आपको मेरा नमस्कार है। आप
- **Translation**: 

---

### Verse 19 (Bramha 0.4039)
- **Original**: रहनेवाले जीवसमुदायका क्लेश निवारण करनेमें ही जन्मदाता हैं और आप ही जन्म लेनेवाले
- **Translation**: 

---

### Verse 20 (Bramha 0.4040)
- **Original**: दक्ष हैं। कृपानिधे! विष्णो ! आप मेरे मस्तकपर प्राण्योंके भीतर निवास करते हैं। आपकी जय
- **Translation**: 

---

