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

### Verse 1 (Vaivtpuran 543.13674)
- **Original**: दी और शिवने अपनी अमृतमयी दृष्टिसे देखकर देखा-शंकर अत्यन्त सुन्दर रूप और वेशभूषासे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13675)
- **Original**: भस्मके उस ढेरसे पुनः कामदेवको प्रकट कर सुशोभित हैं। उनका प्रत्येक अड्ग रब्ननिर्मित । दिया। तत्पश्चात्‌ योगियोंके परम गुरु निर्विकार आभूषणोंसे विभूषित है। चन्दन, अगुरु, कस्तूरी भगवान्‌ शंकरने उन परिहासपरायणा देवियोंसे तथा कुंकुमसे अलंकृत है। उनके प्रसन्नमुखपर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13676)
- **Original**: कहा-- आप सब-की-सब साध्वी तथा जगन्माताएँ मन्द मुस्कानकी प्रभा फैल रही है। वे कटाक्षपूर्वक
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13677)
- **Original**: हैं, फिर मुझ पुत्रके प्रति यह चपलता क्‍यों ?' देखते और मनको हर लेते हैं। उनकी वेश-भूषा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13678)
- **Original**: शिवकी यह बात सुनकर वे देवियाँ सम्भ्रमपूर्वक अपूर्व एवं सूक्ष्म है। वे सिन्दूर-विन्दुओंसे विभूषित
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13679)
- **Original**: चित्रलिखी-सी खड़ी रह गयीं। इसके बाद हैं। उनकी गौर-कान्ति मनोहर चम्पाकी आभाको
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13680)
- **Original**: शंकरजीने भोजन किया। फिर उन्होंने मनोहर तिरस्कृत कर रही है। वे सर्वाड्भसुन्दर, नूतन
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13681)
- **Original**: राजसिंहासनपर विराजमान हो उस दिव्य निवासगृहकी यौवनसे सम्पन्न तथा मुनीन्द्रोंक भी चित्तको मोह अनुपम शोभा एवं चित्रकारी देखी। यह सब लेनेवाले हैं। वहाँ सरस्वती, लक्ष्मी, सावित्री,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13682)
- **Original**: देखकर उन्हें आश्चर्य और परम संतोष हुआ। गड्जा, रति, अदिति, शची, लोपामुद्रा, अरुन्धती,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13683)
- **Original**: रातको उन्होंने उसी दिव्य भवनमें विश्राम किया। अहल्या, तुलसी, स्वाहा, रोहिणी, वसुधादेवी,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13684)
- **Original**: प्राणवल्लभे! जब प्रातःकाल हुआ, तब नाना शतरूपा तथा संज्ञा-ये सोलह देवाड्रनाएँ भी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13685)
- **Original**: प्रकारके याद्योंकी मधुर ध्वनि होने लगी। फिर उपस्थित थीं। इनके सिवा और भी बहुत-सी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13686)
- **Original**: तो सब देवता बेगपूर्वक उठे और बेशभूषासे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13687)
- **Original**: + श्रीकृष्णजन्पखण्ड
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13688)
- **Original**: 595 हि 30040 04404 00400000000400400000 40 4044040.020.4//80
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13689)
- **Original**: ।/।]]/।।//]]
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13690)
- **Original**: /। 44 सज्जित हो अपने-अपने बाहनोंपर सवार होकर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13691)
- **Original**: हैं; अत: मायाका आश्रय ले बारंबार जोर-जोरसे कैलासकी यात्राके लिये उद्यत हो गये। उस समय
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13692)
- **Original**: रोने लगीं। पार्वतीके रोनेसे ही वहाँ सब स्त्रियाँ नारायणको आज्ञासे धर्म उस वासभवनमें गये और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13693)
- **Original**: रोने लगीं। पत्नियों तथा सेवकगर्णोंसहित सम्पूर्ण योगीश्वर शंकरसे समयोचित वचन बोले। [
- **Translation**: 

---

