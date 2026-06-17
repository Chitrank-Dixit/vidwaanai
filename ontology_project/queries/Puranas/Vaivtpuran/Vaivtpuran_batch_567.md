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

### Verse 1 (Vaivtpuran 39.18189)
- **Original**: पश्ललक्षजपेनैव स्तोत्रसिद्धिर्भवेश्रणाम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 39.18190)
- **Original**: महासुखी ऊ् राजेन्द्रो भविष्यति न संशय:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 39.18191)
- **Original**: इति अऔरीब्रह्मवैवर्ते ध्यानपन्त्रसाहितमिद्रकृत लक्ष्मीस्तोत्रं सम्पूर्णम्‌। (प्रकृतिखण्ड 39
- **Translation**: 

---

### Verse 4 (Vaivtpuran 39.18192)
- **Original**: 51--79) +न्‍्ॉन्फाम्दंड >>
- **Translation**: 

---

### Verse 5 (Vaivtpuran 43.17996)
- **Original**: छर्ड + संक्षिप्त ब्रह्मवैयर्तपुराण « ऋ%%ऋ# # ऋऋ # # ऋ# # # # ऋ % # # # # ## # & ### # % ## ## # # # #; ## ## ## ## ######&#& #### 6 #####&# कक कक शिवेन कृतं प्रकृत्या: स्तोत्रम्‌ महे श्वर उवाच 3» नमः प्रकृत्यै ( मन्त्र: )। ब्राहि ब्रह्मस्वरूपे त्व॑ मां प्रसीद सनातनि । भद्रे भद्गप्रदे दुर्गे दुर्गप्ते दुर्गनाशिनि । सर्वस्वरपे . सर्वेशि सर्वबीजस्वरूपिणि । सर्वमड्रलरूपे.. च सर्वमड्रलदायिनि । निद्रे तत्दे क्षमे श्रद्धे तुष्टिपुष्टिस्थरूपिणि । बेदस्वरूपे वेदानां कारणे वेददायिनि । दये जये महामाये प्रसीद जगदप्बिके । लक्ष्मीनारायणक्रोडे.. स्रप्रर्यक्षसि. भारति । कलाकाष्टास्वकपे चर दिवारात्रिस्वरूपिणि । कारणे सर्वशक्तीनां कृष्णस्थोरसि राधिके । यशःस्वरूपे यशसां कारणे च यज्ञःप्रदे । समस्तकामिनीरूपे कलांशेन प्रसीद में । प्रसीद परमानन्दे कारणे सर्वसम्पदाम्‌ । आधारें सर्वजगतां रत्राथारें. वसुन्धरे । योगस्वरूपे योगीशे योगदे योगकारणे । सर्वसिद्धिस्वकपे च सर्वसिद्धिप्रदायिनि । व्याख्यान सर्वशास्त्राणां मतभेदे महेश्वरि । केचिद्‌ बदन्ति प्रकृते: प्राधान्यं पुरुषस्य च
- **Translation**: 

---

### Verse 6 (Vaivtpuran 43.17997)
- **Original**: महाविष्णोनांभिदेशे स्थितं त॑ कमलोद्धवम्‌ । दृष्टा स्तुति प्रकुर्यन्त ब्रह्माणं रक्षितुं पुरा । नारायणस्त्वया शक्त्या जघान तौ महासुरो । पुरा अतिपुरसंग्रामे गगनात्‌ पतिते मयि । अधुना रक्ष मामीशे प्रदग्ध॑ विरहाग्रिना । परमात्मस्वरूपे च्च परमानन्दरूपिणि
- **Translation**: 

---

### Verse 7 (Vaivtpuran 43.17998)
- **Original**: पोतस्वरूपे5जीर्णे त्व॑ मां प्रसीद ॒भवार्णवे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 43.17999)
- **Original**: सर्वाधारे सर्वविद्ये मां प्रसीद जयप्रदे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 43.18000)
- **Original**: समस्तमड्ुलाधारे प्रसीद सर्वपड्नले
- **Translation**: 

---

### Verse 10 (Vaivtpuran 43.18001)
- **Original**: लज्जे मेथे बुद्धिरूपे प्रसीद भक्तवत्सले
- **Translation**: 

---

### Verse 11 (Vaivtpuran 43.18002)
- **Original**: सर्ववेदाड्रूपे च॑ बेदमातः प्रसीद मे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 43.18003)
- **Original**: क्षान्ते शान्ते च सर्वान्ति भ्षुत्पिपासास्वरूपिणि
- **Translation**: 

---

### Verse 13 (Vaivtpuran 43.18004)
- **Original**: मम क्रोडे महामाये विष्णुमाये प्रसीद मे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 43.18005)
- **Original**: परिणामप्रदे देवि प्रसीद दीनवत्सले
- **Translation**: 

---

### Verse 15 (Vaivtpuran 43.18006)
- **Original**: कृष्णप्राणाधिके भद्ठे प्रसीदकृष्णपूजिते
- **Translation**: 

---

### Verse 16 (Vaivtpuran 43.18007)
- **Original**: सर्वदेवीस्वरूपे. च _नारीरूपविधायिनि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 43.18008)
- **Original**: सर्वसम्पत्स्यरूपे च. सर्वसम्पत्प्रदे शुभे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 43.18009)
- **Original**: अशस्विनां पूजिते चर प्रसीद यशसां निधे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 43.18010)
- **Original**: चराचरस्वरूपे चर प्रसीद मम मा चिरम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 43.18011)
- **Original**: योगाधिष्ठात्रि देवीशे प्रसीद सिद्धयोगिनि
- **Translation**: 

---

