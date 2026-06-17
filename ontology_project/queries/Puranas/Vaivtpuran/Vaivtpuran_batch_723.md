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

### Verse 1 (Vaivtpuran 543.12774)
- **Original**: निवासियोंने उन भारतीदेवीको देखा। वे कौतृूहलसे तुम शीघ्र मेरे परात्पप धाम गोलोककों जाओ।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12775)
- **Original**: भरी हुई, परम सुन्दरी, रमणीया तथा श्वेतवर्णा वहाँ प्रकृतिकी अंशरूपा मड्जगलदायिनी भारतीकों
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12776)
- **Original**: थीं। उनके मुखपर मन्द मुस्कानकी प्रभा फैल पाओगे। कल्याण-सृष्टिकी बीजरूपिणी प्रकृतिको
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12777)
- **Original**: रही थी। मुख शरद्‌ ऋतुके चन्द्रमाकों लज्जित अपनाओ। अहो ! तुमने एक कल्पतक तप किया
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12778)
- **Original**: कर रहा था। नेत्र शरद्‌ ऋतुके प्रफुल्ल कमलोंके है तो भी इस समय एक अप्सराके शापसे कोई
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12779)
- **Original**: समान जान पड़ते थे। दीप्तिमानू ओष्ठ और भी तुम्हारे मन्त्रको नहीं ग्रहण करते हैं। अन्य
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12780)
- **Original**: अधरपज्लब पके बिम्बफलकी प्रभाको छीने लेते देवताओंकी पूजामें भी तुम्हारी ही पूजा होगी;
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12781)
- **Original**: थे। मुक्तापंक्तिकी शोभाकों तिरस्कृत करनेवाली क्योंकि तुम्हीं जगतके धारण-पोषण करनेवाले,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12782)
- **Original**: दन्तपंक्तियोंसे उनके मुखकी मनोहरता बढ़ गयी स्वात्माराम, सर्वरूपी तथा सब ओर समस्त देहोंमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12783)
- **Original**: थी। रत्ननिर्मित केयूर-कंगन हाथोंकी और रत्नोंके पूजास्वरूप हो। नूपुर चरणोंकी शोभा बढ़ाते थे। रत्रमय युगल उस समय मेरी आज्ञा मानकर जगदुरु ब्रह्माते
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12784)
- **Original**: कुण्डलॉसे कानोंके नीचेके भाग झलमला रहे थे।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12785)
- **Original**: 560 * संक्षिप्त ्रह्मवैवर्तपुराण *
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12786)
- **Original**: %#&#####%ऋ%% 4 # # ##&#####ऋऋ#ऋ% 4 ##%# ###ऋऋऋकऊऋऊऋऊ$ऋकक््््क्ऋऋपऋ कक #ऋ 4 ऋ 8
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12787)
- **Original**: कक र्रेन्द्रसारनिर्मित हारसे उनका वक्ष:स्थल अत्यन्त
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12788)
- **Original**: और उनके प्रत्येक मुखमें तीन-तीन नेत्र शोभा प्रकाशमान दिखायी देता था। वे अग्रिशुद्ध सूक्ष्म पाते हैं। हाथोंमें त्रिशूल और पद्टिश हैं। वस्त्र धारण करके नूतन यौवनसे सम्पन्न एवं कटिभागमें व्याप्रचर्ममय वस्त्र शोभा पाता है। अत्यन्त कमनीय दृष्टिगोचर होती थीं। उनके दो
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12789)
- **Original**: वे श्वेत कमलके बीजकी मालासे स्वयं ही हाथोंमें वीणा और पुस्तक तथा अन्य हाथोंमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12790)
- **Original**: अपने-आपका-अपने मन्त्रोंका जप करते हैं। व्याख्याकी मुद्रा देखी जाती थी। ब्रह्मलोकनिवासियोंने
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12791)
- **Original**: उनके प्रसन्न मुखपर मन्द हास्यकी छटा छायी उनपर प्रिय वस्तुएँ निछावर करके परम मज़लमय
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12792)
- **Original**: रहती है। वे परात्पर शिव मस्तकपर अर्धचन्द्रका उत्सव मनाया और ब्रह्मा तथा भारतीको वे सानन्द
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12793)
- **Original**: मुकुट तथा सुनहरे रंगकी जटाओंका भार धारण पुरीके भीतर ले गये।
- **Translation**: 

---

