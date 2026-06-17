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

### Verse 1 (Vaivtpuran 4.9087)
- **Original**: महाविष्णुके एक-एक रोम-कूपमें एक-एक योग्यता रखते हैं। नेत्रहीन होकर भी सबको देखते
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.9088)
- **Original**: ब्रह्माण्ड है, वे भी आपके ही सोलहवें अंश हैं। हाथ और मुखसे रहित होकर भी भोजन
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.9089)
- **Original**: हैं। समस्त योगीजन आपके इस मनोबाउिछत करते हैं। आप तेजोमय परमात्माको-मेरा नमस्कार
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.9090)
- **Original**: ज्योतिर्मय स्वरूपका ध्यान करते हैं। परंतु जो है। वेदमें जिस वस्तुका निरूपण है, विद्वान्‌ पुरुष
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.9091)
- **Original**: आपके भक्त हैं, वे आपकी दासतामें अनुरक्त उसीका वर्णन कर सकते हैं। जिसका बेदमें भी रहकर सदा आपके चरणकमलॉकी सेवा करते निरूपण नहीं हो सका है, आपके उस तेजोमय
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.9092)
- **Original**: हैं। परमेश्व! आपका जो परम सुन्दर और स्वरूपको मैं नमस्कार करता हूँ। कमनीय किशोर-रूप है, जो मन्त्रोक्त ध्यानके जो सर्वेश्वर है, किंतु जिसका ईश्वर कोई
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.9093)
- **Original**: अनुरूप है, आप उसीका हमें दर्शन कराइये। नहीं है; जो सबका आदि है, परंतु स्वयं आदिसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.9094)
- **Original**: जिसकी अड्भकान्ति नूतन जलधरके समान श्याम रहित है तथा जो सबका आत्मा है, किंतु जिसका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.9095)
- **Original**: है, जो पीताम्बरधारी तथा परम सुन्दर है, जिसके आत्मा दूसरा कोई नहीं है; आपके उस तेजोमय
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.9096)
- **Original**: दो भुजाएँ, हाथमें मुरली और मुखपर मन्द-मन्द स्वरूपको मैं नमस्कार करता हूँ। मैं स्वयं
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.9097)
- **Original**: मुसकान है, जो अत्यन्त मनोहर है, माथेपर जगत्‌का स्रष्टा और वेदोंकों प्रकट करनेवाला हूँ।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.9098)
- **Original**: मोरपंखका मुकुट धारण करता है, मालतीके धर्मदेव जगत्‌के पालक हैं तथा महादेवजी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.9099)
- **Original**: पुष्पसमूहोंसे जिसका श्रृड्गार किया गया है, जो संहारकारी हैं; तथापि हममेंसे कोई भी आपके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.9100)
- **Original**: चन्दन, अगुरु, कस्तूरी और केसरके अड्भरागसे उस तेजोमय स्वरूपका स्तवन करनेमें समर्थ नहीं
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.9101)
- **Original**: चर्चित है, अमूल्य रत्रोंके सारतत्त्वसे निर्मित है। आपको सेवाके प्रभावसे वे धर्मदेव अपने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.9102)
- **Original**: आभूषणोंसे विभूषित है, बहुमूल्य रत्नोंके बने हुए रक्षककी रक्षा करते हैं। आपकी ही आज्ञासे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.9103)
- **Original**: किरीट-मुकुट जिसके मस्तककों उद्धासित कर आपके द्वारा निश्चित किये हुए समयपर महादेवजी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.9104)
- **Original**: रहे हैं, जिसका मुखचन्द्र शरत्कालके प्रफुल्ल जगतूका संहार करते हैं। आपके चरणारविन्दोंकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.9105)
- **Original**: कमलॉंकी शोभाको चुराये लेता है, जो पके सेवासे ही सामर्थ्य पाकर मैँ प्राणियोंके प्रारब्ध बिम्बफलके समान लाल ओठोंसे सुशोभित है, या भाग्यकी लिपिका लेखक तथा कर्म करनेवालोंके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.9106)
- **Original**: परिपक्व अनारके बीजको भाँति चमकीली फलका दाता बना हुआ हूँ। प्रभो! हम तीनों
- **Translation**: 

---

