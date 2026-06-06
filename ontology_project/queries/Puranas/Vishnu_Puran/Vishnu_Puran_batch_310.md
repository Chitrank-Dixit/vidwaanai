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

### Verse 1 (Vishnu Puran 0.6181)
- **Original**: हे ट्विज ! एक दिन कार्तिकी पूर्णिमाको उपवास कर उन दोनों पति-पल्नियोंने श्रीगढ्ञाजीमे एक साथ ही स््रान करनेके अनन्तर बाहर आनेपर एक पाषण्डीको सामने आता देस्वा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6182)
- **Original**: यह ब्राह्मण उस महात्मा राजाके धनुर्वेदाचार्यका मित्र था; अतः आचार्यके गौरववद राजाने भी उससे मित्रवत्‌ व्यवहार किया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6183)
- **Original**: किन्तु उसकी पतित्नता पत्नीने उसका कुछ भी आदर नहीं किया; वह मौन रही और यह सोचकर कि मैं उपोष्तिता (उपवासयुक्त) हूँ उसे देखकर सूर्यका दर्शन किया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6184)
- **Original**: हे द्विजोत्तम ! फिर
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6185)
- **Original**: डन स्त्री-पुरुषोंनि यथारोति आकर भगबान्‌ विष्णुके पूजा आदिक सस्पूर्ण कर्म विधिपूर्वक किये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6186)
- **Original**: काल्ान्तरगें बह झप्रुजित्‌ राजा मर गया। तब, देवी जैव्याने भी चितारूढ़ महाराजका अनुगभन क्तिया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6187)
- **Original**: आ0 18 ] स तु तेनापचारेण श्वा जल्ले बसुधाधिपः । तृत्तीय अंश 55 राजा शातधनुने उपवास-अवस्थामें पाखण्डीसे उपोषितेन पाषण्डसैल्लापो यत्कृतो3भवत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6188)
- **Original**: वार्तात्पप किया था। अतः उस पापके कारण उसने सा तु जातिस्मरा जज्ञे काशीराजसुता शुभा । सर्वविज्ञानसम्पूर्णा. सर्वलक्षणपूजिता
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6189)
- **Original**: 63 तां पिता दातुकामो5भूद्राय विनिवारितः । तयैव तन्व्या विरतो विवाहारम्भतो नृप:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6190)
- **Original**: 64 ततस्सा दिव्यया दृष्ट््चा दृष्ठा श्वान॑ निज॑ पतिम्‌ । विदिशाख्यं पुरं गत्वा तदवर्स्थं ददर्श तम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6191)
- **Original**: 65 त॑ दृष्ठैंव महाभागं श्वभूत॑ तु पति तदा। ददो तस्मे बराहारं सत्कारप्रवर्ण शुभा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6192)
- **Original**: 66 भुझन्दत्त तया सो5न्नमतिमृष्टमभीप्सितम्‌ । स्वजातिललितं कुर्बन्बहु चादु चकार वे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6193)
- **Original**: 67 अतोव ब्रोडिता बाला कुर्वता चादु तेन सा । अ्रणामपूर्वमाहेदें दयित ते कुयोनिजम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6194)
- **Original**: 68 स्मर्यतां तन्महाराज दाक्षिण्यछलितं त्वया । येन श्वयोनिमापन्नो मम चादुकरो भवान्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6195)
- **Original**: 69 पाषण्डिन समाभाष्य तीर्थस््नानादनन्तरम्‌। ब्राप्तोडसि कुत्सितां योनि किन्न स्मरसि तत्यभो
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6196)
- **Original**: । 70 अश्रीपराशर उवाच तयैव स्मारिते तस्मिन्पूर्वजातिकृते तदा। दध्यौ चिरमथावाप निर्वेदमतिदुर्लभम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6197)
- **Original**: 79 निर्विण्णचित्तस्स ततो निर्गम्य नगराहहि: । मरुत्प्रपतन॑ कुत्वा शार्गाल्लीं योनिमागतः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6198)
- **Original**: 72 सापि द्वितीये सम्प्राप्ते वीक्ष्य दिव्येन चक्षुषा । ज्ञाल्वा श्रूगाल॑ त॑ द्रर्ठैं ययो कोलाहलं गिरिम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6199)
- **Original**: 73 तत्रापि दृष्ठा त॑ प्राह शार्गार्ल्ली योनिमागतम्‌ । भर्त्तारमपि चार्वड्री तनया 'पृथिवीक्षितः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6200)
- **Original**: छड अपि स्मरसि राजेन्र श्वयोनिस्थस्थ यन्मया । ज्ोक्ते ते पूर्वचरित॑ पाषण्डालापसंश्रयम्‌
- **Translation**: 

---

