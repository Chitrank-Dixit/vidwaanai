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

### Verse 1 (Vaivtpuran 543.12514)
- **Original**: निर्मित नूपुरोँंकी सम्मिलित झनकार कुछ कालतक रासमण्डलमें प्रवेश किया। राधाकों अपने समीप
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12515)
- **Original**: निरन्तर होती रहो। इस प्रकार स्थलमें रासक्रीड़ा देखकर श्रीकृष्ण वहाँ बड़े प्रसन्न हुए। वे बड़े प्रेमसे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12516)
- **Original**: करके वे सब प्रसन्नतापूर्वक जलमें उतरे और मुस्कराते हुए उनके निकट गये। उस समय प्रेमसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12517)
- **Original**: वहाँ जल-क्रौड़ा करते-करते थक गये। फिर आकुल हो रहे थे। राधा अपनी सखियोंके बीचमें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12518)
- **Original**: बहाँसे निकलकर नवीन वस्त्र धारण करके रत्नमय अलंकारोंसे विभूषित होकर खड़ी थीं।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12519)
- **Original**: कौतूहलपूर्वक कर्पूरयुक्त ताम्बूल ग्रहण करके उनके श्रीअद्भोंपर दिव्य वस्त्रोंके परिधान शोभा पा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12520)
- **Original**: सबने रत्नमय दर्पणमें अपना-अपना मुँह देखा। रहे थे। वे मुस्कराती हुई बाकी चितवनसे श्यामसुन्दरकी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12521)
- **Original**: तदनन्तर श्रीकृष्ण राधिका तथा गोपियोंके साथ ओर देखती हुई गजराजकी भाँति मन्द गतिसे चल
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12522)
- **Original**: नाना प्रकारकी मधुर-मनोहर क्रौड़ाएँ करने लगे। रही थीं। रमणीय राधा नवीन वेशभूषा, नयी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12523)
- **Original**: । फिर पतित्र उद्यानके निर्जन प्रदेशमें सरोवरके अवस्था तथा रूपसे अत्यन्त मनोहर जान पड़ती
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12524)
- **Original**: रमणीय तटपर जहाँ बाहर चन्द्रमाका प्रकाश फैल थीं। वे मुनियोंके मनको भी मोह लेनेमें समर्थ थीं।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12525)
- **Original**: रहा था, जहाँकी भूमि पुष्प और चन्दनसे चर्चित उनकी अड्जगकान्ति सुन्दर चम्पाके समान गौर थी।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12526)
- **Original**: थी, जहाँ सब ओर अगुरु तथा चन्दनसे सम्पृक्त मुख शरत्पूर्णिमाके चन्द्रमाकों लज्जित कर रहा था।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12527)
- **Original**: मलय-समीरद्वारा सुगन्‍न्ध फैलायी जा रही थी और वे सिरपर मालतीकीौ मालासे युक्त बेणीका भार
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12528)
- **Original**: भ्रमरोंके गुझ्लारवके साथ नर-कोकिलोंकी मधुर वहन करती थीं। काकली कानोंमें पड़ रही थी; योगियोंके परम गुरु
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12529)
- **Original**: + भ्रीकृष्णजन्मखण्ड * 549
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12530)
- **Original**: ]]])0]]8]4]0]0]]224] 0] 2
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12531)
- **Original**: 6 । 444 श्यामसुन्दर श्रीकृष्णे अनेक रूप धारण करके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12532)
- **Original**: करने लगीं। स्मणीय पुष्पोद्यान, सरोवरोंके तट, स्थल-प्रदेशमें मधुर लीला-विलास किये। इसके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12533)
- **Original**: सुरम्य गुफा, नदों और नदियोंके समीप, अत्यन्त बाद राधाके साथ सनातन पूर्णब्रह्मस्वरूप श्रीकृष्णने
- **Translation**: 

---

