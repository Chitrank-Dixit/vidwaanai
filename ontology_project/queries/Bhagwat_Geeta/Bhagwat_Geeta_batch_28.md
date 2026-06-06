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

### Verse 1 (Bhagwat_Geeta 7.704)
- **Original**: न मां दुष्कृतिनो मूढाः प्रपद्यन्ते नराधमा:। माययापहतज्ञाना आसुरं भावमाश्निताः
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 7.705)
- **Original**: मायाके द्वारा जिनका ज्ञान हरा जा चुका है ऐसे आसुर-स्वभावको धारण किये हुए, मनुष्योंमें नीच, दूषित कर्म करनेवाले मूढ़लोग मुझको नहीं भजते
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 7.706)
- **Original**: चतुर्विधा भजन्ते मां जनाः सुकृतिनोअर्जुन। आर्तो जिज्ञासुरर्थार्थी ज्ञानी च भरतर्षभ
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 7.707)
- **Original**: हे भरतवंशियोंमें श्रेष्ठ अर्जुन ! उत्तम कर्म करनेवाले
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 7.708)
- **Original**: * अध्याय 7 * 103 अर्थार्थी,, आर्त', जिज्ञासु और ज्ञानी--ऐसे चार प्रकारके भक्तजन मुझको भजते हैं
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 7.709)
- **Original**: तेषां ज्ञानी नित्ययुक्त एकभक्तिर्विशिष्यते। प्रियो हि ज्ञानिनो5त्यर्थमहं स च्व मम प्रिय:
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 7.710)
- **Original**: उनमें नित्य मुझमें एकौभावसे स्थित अनन्य प्रेमभक्तिवाला ज्ञानी भक्त अति उत्तम है, क्योंकि मुझको तत्त्वसे जाननेवाले ज्ञानीको मैं अत्यन्त प्रिय हूँ और वह ज्ञानी मुझे अत्यन्त प्रिय है
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 7.711)
- **Original**: उदाराः सर्व एवैते ज्ञानी त्वात्मैव मे मतम्‌। आस्थितः स हि युक्तात्मा मामेवानुत्तमां गतिम्‌
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 7.712)
- **Original**: ये सभी उदार हैं, परन्तु ज्ञानी तो साक्षात्‌ मेरा स्वरूप ही है--ऐसा मेरा मत है; क्योंकि वह मद्गत मन-बुद्धिवाला ज्ञानी भक्त अति उत्तम गतिस्वरूप मुझमें ही अच्छी प्रकार स्थित है
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 7.713)
- **Original**: बहूनां जन्मनामन्ते ज्ञानवान्मां प्रपद्यते। वासुदेव: सर्वमिति स महात्मा सुदुर्लभ:
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 7.714)
- **Original**: बहुत जन्मोंके अन्तके जन्ममें तत्त्वज्ञानको प्राप्त 1. सांसारिक पदार्थोके लिये भजनेवाला। 2. संकट-निवारणके लिये भजनेवाला। 3. मेरेको यथार्थरूपसे जाननेकी इच्छासे भजनेवाला।
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 7.715)
- **Original**: 104 * श्रीमद्धगवद्रीता * पुरुष, सब कुछ वासुदेव ही है--इस प्रकार मुझको भजता है, वह महात्मा अत्यन्त दुर्लभ है
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 7.716)
- **Original**: कामैस्तैस्तैईतज्ञाना: प्रपद्यन्तेडन्यदेवता: । तं त॑ं नियममास्थाय प्रकृत्या नियताः स्वया
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 7.717)
- **Original**: उन-उन भोगोंकी कामनाद्वारा जिनका ज्ञान हरा जा चुका है, वे लोग अपने स्वभावसे प्रेरित होकर उस-उस नियमको धारण करके अन्य देवताओंको भजते हैं अर्थात्‌ पूजते हैं
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 7.718)
- **Original**: योयो यां यां तनुं भक्त: श्रद्धयार्चितुमिच्छति। तस्य तस्याचलां श्रद्धां तामेव विद्धाम्यहम्‌
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 7.719)
- **Original**: जो-जो सकाम भक्त जिस-जिस देवताके स्वरूपको श्रद्धासे पूजना चाहता है, उस-उस भक्तकी श्रद्धाको मैं उसी देवताके प्रति स्थिर करता हूँ
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 7.720)
- **Original**: स तया श्रद्धया युक्तस्तस्याराधनमीहते। लभते च तत: कामान्मयैव विहितान्हि तान्‌
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 7.721)
- **Original**: वह पुरुष उस श्रद्धासे युक्त होकर उस देवताका पूजन करता है और उस देवतासे मेरे द्वारा ही विधान किये हुए उन इच्छित भोगोंको निःसन्देह प्राप्त करता है
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 7.722)
- **Original**: अन्तवत्तु फल॑ तेषां तद्धवत्यल्पमेधसाम्‌। देवान्देवयजो यान्ति मद्धक्ता यान्ति मामपि
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 7.723)
- **Original**: * अध्याय 7 * 5105 परन्तु उन अल्प बुद्धिवालोंका वह फल नाशवान्‌ है तथा वे देवताओंको पूजनेवाले देवताओंको प्राप्त होते हैं और मेरे भक्त चाहे जैसे ही भें, अन्तमें वे मुझको ही प्राप्त होते हैं
- **Translation**: 

---

