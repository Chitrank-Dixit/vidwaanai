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

### Verse 1 (Nard Puran 0.1261)
- **Original**: *रम' आदि धातु अनुदत्तेत्‌ हैं और 'जिधि्विदा' उदात्तेत्‌ है। स्कम्भु आदि पंद्रह धातु परस्मैपदी हैं
- **Translation**: 

---

### Verse 2 (Nard Puran 0.1262)
- **Original**: कित' धातु ' उदात्तेतु' है। 'दान' 'शान -ये अनुदात्तेत्‌ (आत्मनेषदी) बताये गये हैं। 'गुप्‌'
- **Translation**: 

---

### Verse 3 (Nard Puran 0.1263)
- **Original**: दो धातु उभयपदी हैं। “पच' आदि नौ धातु
- **Translation**: 

---

### Verse 4 (Nard Puran 0.1264)
- **Original**: पूर्वभाग-द्वितीय पाद स्वरितेत्‌ (उभयपदी) हैं। वे परस्मैपदी (और आत्मनेपदी दोनों) माने गये हैं
- **Translation**: 

---

### Verse 5 (Nard Puran 0.1265)
- **Original**: फिर तीन स्वरितेत्‌ धातु हैं। परिभाषणार्थक “बद' और “बच' धातु परस्मैपदी हैं। ये एक हजार छ: धातु भ्वादि कहे गये हैं
- **Translation**: 

---

### Verse 6 (Nard Puran 0.1266)
- **Original**: 'अद' और 'हन्‌' धातु परस्मैपदी कहे गये हैं। *द्विष' आदि चार धातु स्वरितेत्‌ माने गये हैं
- **Translation**: 

---

### Verse 7 (Nard Puran 0.1267)
- **Original**: यहाँ केवल 'चक्षिड” धातु आत्मनेपदी कहा गया है। फिर 'ईर' आदि तेरह धातु अनुदात्तेतू हैं
- **Translation**: 

---

### Verse 8 (Nard Puran 0.1268)
- **Original**: मुने! वैयाकरणोंने 'घुडरं और 'शीड्/-इन दो धातुओंको आत्मनेपदी कहा है। फिर “घु' आदि सात धातु परस्मैपदी बताये गये हैं
- **Translation**: 

---

### Verse 9 (Nard Puran 0.1269)
- **Original**: मुनीश्वर ! यहाँ एक “ऊर्णुज्‌' धातु स्वरितेत्‌ कहा गया है। 'द्यु' आदि तीन धातु परस्मैपदी बताये गये हैं
- **Translation**: 

---

### Verse 10 (Nard Puran 0.1270)
- **Original**: नारद। केवल 'ट्रज्‌' धातुको शाब्दिकोंने उभयपदी कहा है
- **Translation**: 

---

### Verse 11 (Nard Puran 0.1271)
- **Original**: “रा' आदि अठारह धातु परस्मैपदी माने गये हैं। नारद! फिर केवल 'इड्/ धातु आत्मनेपदी कहा गया है
- **Translation**: 

---

### Verse 12 (Nard Puran 0.1272)
- **Original**: उसके बाद 'विद' आदि चार धातु परस्मैपदी माने गये हैं। “जिष्वप्‌ शये' यह धातु परस्मैपदी कहा गया है
- **Translation**: 

---

### Verse 13 (Nard Puran 0.1273)
- **Original**: मुने ! *श्रस” आदि धातु मैंने तुम्हें परस्मैपदी कहे हैं। “दोधीड्‌” और “वेवीड्र--ये दो धातु आत्मनेपदी माने गये हैं
- **Translation**: 

---

### Verse 14 (Nard Puran 0.1274)
- **Original**: 'पस' आदि तीन धातु 'उदात्तेतू' हैं। मुनिश्रेष्ठ! “चर्करीतं च' यह यडूलुगन्तका प्रतीक है। यह अदादि माना गया है। 'हड्‌ धातु अनुदात्तेत्‌ कहा गया है
- **Translation**: 

---

### Verse 15 (Nard Puran 0.1275)
- **Original**: इस प्रकार अदादि गणमें तिहत्तर धातु बताये गये हैं। “हु” आदि चार धातु (हु, भी, ही और पृ) परस्मैपदी माने गये हैं
- **Translation**: 

---

### Verse 16 (Nard Puran 0.1276)
- **Original**: ' भृज्‌' धातु स्वरितेत्‌ और “ओहाक्‌' धातु उदात्तेत्‌ है। “माइ” और 'ओहाडइ्‌'-ये दोनों धातु अनुदात्तेत्‌ हैँ। दानार्थक 'दा' और धारणार्थक ' धा'--इनमें स्वर्तिको इत्संज्ञा हुई है
- **Translation**: 

---

### Verse 17 (Nard Puran 0.1277)
- **Original**: 'णिजिर' आदि तीन धातु स्वसितित्‌ 239 कहे गये हैं। 'घृ' आदि बारह धातु परस्मैपदी माने गये हैं
- **Translation**: 

---

### Verse 18 (Nard Puran 0.1278)
- **Original**: इस प्रकार ह्लादि (जुहोत्यादि) गणमें बाईस धातु कहे गये हैं। *दिव्‌' आदि पचीस धातु परस्मैपदी कहे गये हैं
- **Translation**: 

---

### Verse 19 (Nard Puran 0.1279)
- **Original**: नारद ! 'घूड्‌॑ आदि ' दूड/--ये आत्मनेपदी हैं। 'घूडुन आदि सात धातु ओदित्‌ और आत्मनेपदी माने गये हैं
- **Translation**: 

---

### Verse 20 (Nard Puran 0.1280)
- **Original**: विप्रवर! “लीड” आदि धातु यहाँ आत्मनेपदी बताये गये हैं। श्यति (शो) आदि चार धातु परस्मैपदी हैं
- **Translation**: 

---

