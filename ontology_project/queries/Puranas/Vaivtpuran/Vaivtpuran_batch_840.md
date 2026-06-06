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

### Verse 1 (Vaivtpuran 543.15114)
- **Original**: मलत्याग न करे। बाँबीसे निकली हुई, चूहेको अश्वमेध-यज्ञका फल पाता है। जो एकादशी और
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15115)
- **Original**: खोदी हुई, पानीके भीतरसे निकाली हुई, शौचसे कृष्णजन्माष्टमीका न्रत करते हैं, वे सौ जन्मोंके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15116)
- **Original**: बची हुई और घरके लीपनेसे प्राप्त हुई मिट्टीको किये हुए पापसे मुक्त हो जाते हैं; इसमें संशय
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15117)
- **Original**: शौचके काममें न ले। जिस मिट्टरीमें चींटी आदि नहीं है। बाल्यावस्था, कुमारावस्था, युवावस्था
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15118)
- **Original**: प्राणी हों, उसे भी शौचके काममें न ले। ब्रजेश्वर ! और वृद्धावस्थामें भी जो-जो पाप बन गये हैं, वे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15119)
- **Original**: हल चलानेसे उखड़ी हुई, पौधोंके थालेसे निकाली सब भस्म हो जाते हैं। रोगी, अत्यन्त वृद्ध और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15120)
- **Original**: हुई, जिस खेतमें खेती लहलहा रही हो उसकी बालकके लिये उपवासका नियम नहीं है। भक्त
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15121)
- **Original**: मिट्टी, वृक्षकों जड़से खोदकर ली हुई मिट्टी तथा ब्राह्मणकों द्विगुण भोजनका दान करके दाता शुद्ध
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15122)
- **Original**: वदीके पेटेसे निकाली हुई मृत्तिका-इन सबको
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15123)
- **Original**: 656 + संक्षिम ग्रह्मवैवर्तपुराण « ऋकऊऋ$ऋऊऋऋ कक कक ्क्ऋऋऋ्#5/45%&/ 75% ##%###%#####/##/## 57558 ####/#%##%### ## 6 #%
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15124)
- **Original**: शौचके काममें त्याग देना चाहिये। कुम्हड़ा काटने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15125)
- **Original**: पूजित प्रियतम शिवकी निनन्‍्दा करते हैं, वे सौ या फोड़नेवाली स्त्री और दीपक बुझानेवाले पुरुष
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15126)
- **Original**: ब्रह्माऑंको आयुपर्यन्त नरककी यातना भोगते हैं। कई जन्मोंतक रोगी होते हैं और जन्म-जन्ममें समस्त प्रियजनोंमें ब्राह्मण मुझे अधिक प्रिय हैं। दरिद्र रहते हैं। दीपक, शिवलिड्र, शालग्राम,
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15127)
- **Original**: ब्राह्मणसे अधिक शंकर प्रिय हैं। मेरे लिये शंकरसे मणि, देवप्रतिमा, यज्ञोपवीत, सोना और शड्ख--इन
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15128)
- **Original**: बढ़कर दूसरा कोई प्रिय नहीं है। “महादेव, सबको भूमिपर न रखे। दिनमें और दोनों
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15129)
- **Original**: महादेव, महादेव '--इस प्रकार बोलनेवाले पुरुषके संध्याओंके समय जो नींद लेता या स्त्री-सहवास
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15130)
- **Original**: पीछे-पीछे मैं नामश्रवणके लोभसे फिरता रहता करता है, वह कई जन्मोंतक रोगी और दरिद्र
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15131)
- **Original**: हूँ। शिव नाम सुनकर मुझे बड़ी तृप्ति होतो है। होता है। मिट्टी, राख, गोबर--इसके पिण्डसे या
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15132)
- **Original**: मेरा मन भक्तके पास रहता है। प्राण राधामय हैं, बालूसे भी शिवलिड्डका निर्माण करके एक बार
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15133)
- **Original**: आत्मा शंकर हैं। शंकर मुझे प्राणोंसे भी अधिक उसकी पूजा कर लेनेवाला पुरुष सौ कल्पोंतक
- **Translation**: 

---

