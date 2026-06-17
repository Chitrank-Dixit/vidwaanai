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

### Verse 1 (Vaivtpuran 6.2519)
- **Original**: घरका स्वामी नौकरसे भी अधिक अधम समझा समय इनका नाम “तुलसी” पड़ा। पहले सरस्वतीके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.2520)
- **Original**: जायगा। घरमें जो बलवान होंगे, उन्होंकों कर्ता शापसे और फिर श्रीहरिकी आज्ञासे इन विश्वपावनी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.2521)
- **Original**: माना जायगा। भाई-बन्धु वे ही समझे जाय॑गे, देवीने अपनी कलाद्ठारा वृक्षमयरूप धारण किया।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.2522)
- **Original**: जिनका सम्बन्ध योनि या जन्मको लेकर होगा, कलिमें पाँच हजार वर्षोंतक भारतवर्षमें रहकर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.2523)
- **Original**: जैसे पुत्र, भाई आदि। (अर्थात्‌ जरा भी दूरके ये तीनों देवियाँ सरित्‌-रूपका परित्याग करके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.2524)
- **Original**: सम्पर्कवालेको लोग भाई-बन्धु भी नहीं बैकुण्ठमें चली जायँगी। काशी तथा वृन्दाबनके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.2525)
- **Original**: मानेंगे।) विद्याध्ययनसे सम्बन्ध रखनेवाले गुरु-
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.2526)
- **Original**: + प्रकृतिखएड * 115 कक %%$%$%#% #% #% %ऋ% %ऋ$%ऋ#फऋ%%$%%ऋक%
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.2527)
- **Original**: ; ऋ#%ऋ%$%ऊऋ%कऋक%ऋऊऋ%ऊऋक%ऊऋक%%#$%$%$%%ऋ%ऊऋ#%ऋऊऋ%ऋऊऋऋ%ऊऋकऋ%ऋ%ऋ$%#%$%$%$%$%$%%% भाई आदिके साथ कोई बात भी नहीं करेगा।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.2528)
- **Original**: वर्षमें ही उनके सिर्के बाल पक जायँगे। बीस पुरुष अपने ही परिवारके लोगोंसे अन्य अपरिचित
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.2529)
- **Original**: वर्षमें उन्हें बुढ़ापा घेर लेगा। कलियुगमें भगवन्नाम व्यक्तियोंकी भाँति व्यवहार करेंगे। ब्राह्मण, बेचा जायगा। मिथ्या दान होगा-मनुष्य अपनी क्षत्रिय, वैश्य और शूद्र-चारों वर्ण अपनी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.2530)
- **Original**: कीर्ति बढ़ानेके लिये दान देकर स्वयं पुनः उसे जातिके आचार-बिचारको छोड़ देंगे। संध्या-
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.2531)
- **Original**: वापस ले लेंगे। देववृत्ति, ब्राह्मणवृत्ति अथवा वन्दन और यज्ञोपवीत आदि संस्कार तो प्राय:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.2532)
- **Original**: गुरुकुलवृत्ति-चाहे वह अपनी दी हुई हो अथवा बंद ही हो जायैँंगे। चारों हो वर्ण म्लेच्छके समान
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.2533)
- **Original**: दूसरेकी--कलिके मानव उसे छीन लेंगे। कलियुगमें आचरण करेंगे। प्रायः सभी लोग अपने शास्त्रोंको मनुष्यको अगम्यागमनमें कोई हिचक न रहेगी। छोड़कर म्लेच्छ-शास्त्र पढ़ेंगे। ब्राह्मण, क्षत्रिय,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.2534)
- **Original**: कलियुगमें स्त्रियों और पतियोंका निर्णय नहीं हो वैश्य और शूद्र-चारों वर्णांक लोग सेवावृत्तिसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.2535)
- **Original**: सकेगा। अर्थात्‌ सभी स्त्री-पुरुषोंमें अवैध व्यवहार जीविका चलायेंगे। सम्पूर्ण प्राणियोंमें सत्यका
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.2536)
- **Original**: होंगे। प्रजा किन्हीं ग्रामों और धनोंपर अपना पूर्ण अभाव हो जायगा। जमीनपर धान्य नहीं उपजेंगे।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.2537)
- **Original**: अधिकार नहीं प्राप्त कर सकेगी। प्रायः सब लोग वृक्ष फलहीन हो जायँगे। गौओंमें दूध देनेकी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.2538)
- **Original**: अप्रिय वचन बोलेंगे। सभी चोर और लम्पट शक्ति नहीं रहेगी। लोग बिना मक्खनके दूधका
- **Translation**: 

---

