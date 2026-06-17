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

### Verse 1 (Markende Puran 0.2201)
- **Original**: 43--87
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2202)
- **Original**: प्रपित्शात 88 # एवं स्तुता तदा देखी तामसी तन्न वेधस्रा
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2203)
- **Original**: लिष्णो: प्रतोथनाथांय निहन्तुं मधुकरैटभी। नेत्रास्थनासिकाशाहुददयरेभ्वस्तश्रोसस;
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2204)
- **Original**: होनेषर जगत्के स्वामी भगवान्‌ जनार्दन उस निर्गप्य दर्शने तस्थौ ब्लह्मणोउव्यक्तजन्मन; । एक्रार्णजबके जलमें शेषनागकी शय्यासे जाग उठे। उत्तस्थीं च्ञ जगन्नाथस्तया मुक्तो जनार्दन:
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2205)
- **Original**: फिर उन्होंने उन दोनों असुरोंको देखा। ले दुरात्पा एकार्णवेडहिशयनाज्षत: स॑ ददृशे चर त्तौ। मधु और कैटभ अत्यन्त क्लवान्‌ तथा पराक्रमों थे मधुकैटभी दुरात्पानावतिवीर्थपराक्रसों
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2206)
- **Original**: 924 और क्रॉधसे लाल आँखें किये ब्रह्माजीकों खा क्रोधरक्तेक्षणाबन्तुं त्रह्माणं जनितोद्म्मी। जानेके लिये उद्योग कर रहे थे। तब भगवात्‌ समुत्थाय ततस्ताभ्यां युयुधे भगचान्‌ हरि:
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2207)
- **Original**: । श्रीहरिने उठकर उन दौनोंके साथ पाँच हजार पञ्मवर्षसहस्राणि वाहुप्रहर्णो. विधु:। ज्र्षोतक केश्नल दाहुयुद्ध किया। वे दोनों भो तावष्यतिकलोन्मत्तौ'। महापरायाविमिोहितौ
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2208)
- **Original**: अत्यन। बल़्के कारण उन्मत्त हो रहे थे। इधर 9. पार-र्णं इन्चूं
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2209)
- **Original**: +बेथा अऋषिका राजा सुरध और सपाधिकोो भगवतीकी महिमा सुनाना« श्थ्5 महामायाने भी उन्हें मोहमें डाल रखा था;
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2210)
- **Original**: एबमेषा सपमुत्पन्ना ब्रह्मणा संस्तुता स्वयम्‌
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2211)
- **Original**: इसलिये वे भगवान्‌ विप्णुसे कहने लगे--हुम तुम्हारी बीखासे संतुष्ट हैं। तुम हमलोगोंसे कोई बर माँगो'
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2212)
- **Original**: 89--95
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2213)
- **Original**: अभगकादुवात
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2214)
- **Original**: भरवेत्तामद्य में तुष्टा प्रम जध्यावुभावषि
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2215)
- **Original**: क्रिमन्बेन वरेणात्र एता्वाद्धि बृते मसे
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2216)
- **Original**: श्रीभगवान्‌ बोले--
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2217)
- **Original**: मद तुम दोनों मुझपर प्रसत् हो तो अन्न मेरे हाथसे मारे जाओ। अस, इतना-सा हो मैंने वर माँगा है। यहाँ दूसरे किसी वस्से क्‍या लेना है
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2218)
- **Original**: 97-98 # ज्षिल्काच # 99 # वच्धिताभ्यामिति तदा सर्वमापोमर्य जगतू
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2219)
- **Original**: विल्तोक्य ताभ्यां गदितों धगवान्‌ कम्रलेक्षण:। आवां जहि च चत्रोर्ची सलिलेन परिप्लुता
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2220)
- **Original**: ऋषि कहते हैं--
- **Translation**: 

---

