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

### Verse 1 (Vishnu Puran 0.9901)
- **Original**: 59 सो5पि कैशोरकबयों मानयन्मरधुसूदनः । रेमे ताभिस्मेयात्मा क्षपासु क्षपिताहित:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9902)
- **Original**: 60 तद्धरतृषपु तथा तासु सर्वभूतेषु चेश्वर:। आत्मस्वरूपरूपो5सौ व्यापी वायुरित स्थित:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9903)
- **Original**: 61 यथा समस्तभूतेषु नभो5भि: पृथिवी जलम्‌ । यायुआत्पा तथैवासो व्याप्य सर्वमवस्थितः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9904)
- **Original**: 62 पञ्मम अंश 37 अपनी बाहुलता श्रोमघुसूदनके गलेमें डाल दी
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9905)
- **Original**: फिसी निपण गोपीने भगवान्‌के गानकी प्रशंसा करनेके खहाने भुजा फैल्म्रकर श्रीमघुसूदनक्तरे आह्फिन करके चूम लिया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9906)
- **Original**: श्रीहरिकी भुजाएँ गोपियोंके कपोलॉका चुम्बन पाकर उन (कपोत्में) में पुछकावलिरूप घान्यकी उत्पत्तिके लिये स्वेट्रूप जल्कके मेघ बन गयीं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9907)
- **Original**: कुष्णचन्द्र जितने उम्रस्तस्से रासोचित गान गाते थे उससे दूने वाव्दसे गोपियाँ ''घन्य कष्ण ! धन्य कृष्ण !!”” की ही ध्यनि लगा रहो थीं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9908)
- **Original**: भगवानके आगे जानेपर गोपियाँ उनके पीछे जातीं और लौटनेपर सामने चलती, इस प्रकार थे अनुलोम और प्रतिलोम-गतिसे श्रीहरिका साथ देती थीं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9909)
- **Original**: -अश्रीमधुसूदन भी गोपियोंके साथ इस प्रकार रासक्रीडा कर रहे थे कि उनके ब्रिना एक क्षण भी गोपियोंकों करोड़ों व्षेकि समान बीतता था
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9910)
- **Original**: थे रास-रसिक गोपाडुनाएँ पति, माता-पिता और भ्राता आदिके रोकनेपर भी रात्रिगें श्रीशयामसुन्दरके श्रीमधुसूदन भी अपनी किद्ोरावस्थाका मान करते हुए, रात्रिकि समय उनके साथ रमण करते थे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9911)
- **Original**: वे सर्वव्यापी ईश्वर श्रीकृष्णचन्द्र गोपियोंमें, उनके पतियोंमें तथा समस्त प्राणियॉमें आत्मस्वरूपसे वायुके समान व्याप्त थे। 61
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9912)
- **Original**: जिस त्रकार आकाश, अप्रि, पृथिवी, जल, वायु और आत्मा समस्त प्राणियोंमें व्याप्त हैं उसी प्रकार वे भी सब पदार्थों व्यापक हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9913)
- **Original**: आप अं पययय इति श्रीविष्णुपुराणे पञ्रमेंडशे त्रयोटशो5्ध्यायः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9914)
- **Original**: न जी अीन चोदहवाँ अध्याय वृषभासुर-व् श्रीपराशर उताच शीपराहरजी बोलछे-- एक दिन सार्यकाह्के समय प्रदोषाग्रे कदाचित्तु रासासक्ते जनार्दने। जब श्रोकृष्णचन्द्र यासक्रीडामें आसक्त थे, अरिष्ट नामक त्रासबन्समदो. गोष्टमरिष्टस्समुपागमत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9915)
- **Original**: एक मदोन्मत असुर [वृषभरूप धारणकर] सबको गी्ठम मत भयभीत करता श्रजमें आया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9916)
- **Original**: इस अरिष्टासुस्की 3र्कलोचन: । कान्ति सजल जलधस्के समान कृष्णवर्ण थी, सौंग स्व॒राग्रपातैरत्यर्थ दारयश्चरणीतलम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9917)
- **Original**: अत्यन्त तीक्षण थे, नेत्र सूर्यके समान तेजस्वों थे और अपने लेलिहानस्सनिष्पेषं जिह्लयोप्ठो पुनः पुनः । खुर्गोंकी चोटले यह मानो प्रथिवीफों फाड़े डालता था
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9918)
- **Original**: वह दाँत पीसता हुआ पुनः पुनः अपनी जिह्नासे संरम्भाविद्धलाडूल: कठिनस्कन्धबन्धन:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9919)
- **Original**: ओठोंको चाट रहा था, उसने क्रोधवश अपनी पुँछ उठा सखि0 प0 12--
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9920)
- **Original**: केडं8 के आजम पुराण धए
- **Translation**: 

---

