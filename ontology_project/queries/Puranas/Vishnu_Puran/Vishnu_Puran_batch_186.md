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

### Verse 1 (Vishnu Puran 0.3701)
- **Original**: उसके अनन्तर नित्यप्रति गात्रि क्षीण होने लगती है और दिन बढ़ने छंगता है । फिर [ मेष तथा वुष ग़शिका अतिक्रमण कर ] मिथुनराहिसे निकलकर उत्तराणणकी अन्तिम सीमापर उपस्थित हो यह कर्कराशिमें दक्षिणायनका आरम्भ करता है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3702)
- **Original**: जिस प्रकार कुल्अछ-चक्रके सिरेपर स्थित जीव अति शीघ्तासे घृूमता है उसी प्रकार सूर्य भी दक्षिणायनको पार करनेमें अति शीघ्रतासे चलता है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3703)
- **Original**: अतः वह अति शौघतापूर्वक वायुवेगसे चलरे हू अपने उत्कृष्ट मार्गको थोड़े समयमें ही पार कर लेता
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3704)
- **Original**: है द्विज! दक्षिणायनमें दिनके समय शीघतापूर्वक चलनेसे उस समयके साढ़े तेरह नक्षत्रॉको सूर्य बारह मुह॒तो
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3705)
- **Original**: ंमिं पार कर लेता है, किन्तु रात्रिके समय (मन्दगार्मा होनेसे) उतने हो नक्षत्रोंकी अठारह मुहू्तोि पार करता है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3706)
- **Original**: कुल्लल-चक्रके मध्यमें स्थित जीव जिस प्रकार धीरे-धीरे चलता है उसी प्रकार उत्तायणके समय सूर्य मन्दगतिसे चलता है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3707)
- **Original**: इसलिये उस समय वह धोड़ी-सी भूमि भी अति दीर्घकालमें पार करता है, अतः उत्तरायणका अन्तिम दिन अठारह मुहूर्तका होता है, उस दिन भी सूर्य अति मन्दगतिसे चलता है और ज्योतिश्षक्रार्धक॑ साढ़े तेरह नक्षत्रोंकी एक दिनमें पार करता है किन्तु रात्रिके समय वह उतने ही (साढ़े तेरह) नक्षत्रोंकी बारह मुड्डूतो
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3708)
- **Original**: ँमिं हो पार कर लेता है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3709)
- **Original**: 36--38
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3710)
- **Original**: अतः जिस प्रकार नाभिदेशमें चक्रके मन्द-मन्द घूमनेसे खहाँका मृत्‌-पिण्ड भी मन्दगतिसे घूमता है उसी प्रकार
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3711)
- **Original**: 132 श्रीविष्णुपुराण [ आअ* 8 कुलालचक्रनाभिस्तु यथा तत्रैव बर्तते
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3712)
- **Original**: धुवस्‍्तथा हि म्रैत्रेय तत्रैव परिवर्तते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3713)
- **Original**: 40 उभयो: काष्ठयोम॑ध्ये भ्रमतो मण्डलानि तु । दिवा नक्त च सूर्यस्य मन्‍्दा शीघ्रा च वै गति:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3714)
- **Original**: 41 मन्दाड़ि यस्पिन्नयने शीघ्रा नक्ते तदा गति: । झीघा निशि यदा चास्य तदा मन्दा दिवा गति:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3715)
- **Original**: 42 एकप्रमाणमेलैष मार्ग याति दिखाकरः । अद्दोराश्रेण यो भुड्ढें समस्‍्ता राशयो छ्विंज
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3716)
- **Original**: 43 षडेव राशीन यो भुड़े रात्रावन्यां श्र मड़दिवा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3717)
- **Original**: उडड राक्षिप्रमाणजनिता दीर्घहुस्वात्मता दिने। तथा निशायां राशीनां प्रमाणैर्लघुदीर्घता
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3718)
- **Original**: 45 दिनादेदीर्घहल्‍स्वत्व॑ तद्धोगेनेव. जायते । उत्तरे प्रक्रमे ज्ञी्रा निशि मन्दा गतिर्दिवा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3719)
- **Original**: 46 दक्षिणे त्वयने चैव विपरीता विवस्वत:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3720)
- **Original**: 47 उषा रात्रि: समाख्याताव्युष्टिश्षाप्युच्यते दिनम्‌ । प्रोच्यते च तथा सन््या उषाव्युष्टच्ोर्यदन्तरम्‌
- **Translation**: 

---

