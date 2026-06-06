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

### Verse 1 (Vishnu Puran 0.9461)
- **Original**: श्रीपराशरजी बोले--सर्पराज कालियसे ऐसा कह भगवान्‌ हरिते उसे छोड़ दिया और यह उन्हें प्रणाम करके समस्त प्राणियोंके देखते-देखते अपने सेवक, पुत्र, बन्धु और र्तियॉके सहित अपने उस कुण्डव ल्लोड़कर समुद्रकों चछा गया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9462)
- **Original**: सर्पके चर जानेपर गोपगण, स्कैटे हुए मृत पुरुषके समान कृष्णचकद्रको आशि्फिनकर प्रोतिपूर्वक उनके मस्तकको नेत्रजछसे भिगोने लगे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9463)
- **Original**: कुछ अत्य गोपगण यमुनाको स्वच्छ जलवाली टेख प्रसन्न होकर लीलाबिहारी विस्मितच्त्तसे स्तुति करने लगे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9464)
- **Original**: तदनन्तर अपने उत्तम चरित्रोंके कारण गोपियॉंसे गीयमान और गोपोंसे प्रशंसित होते हुए कृष्णचन्द्र अजमें चले आये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9465)
- **Original**: न फऔ “"+++ इति श्रीविष्णुपुराणे पशञ्चमेंडइशे सप्तमोडध्यायः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9466)
- **Original**: कजज+ #ऋ
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9467)
- **Original**: आण्8 ] पश्ठम अंश 339 आठवयाँ अध्याय श्रेनुकासुर-बध श्रीपराझर उवाच श्रीपरादरजी बोले--एक दिन बलराम और कृष्ण गा: पालयन्तो च पुनः सहितो बछकेशवो । ढ साथ गौ चराते अति रमणीय तालवनमें आये भ्रममाणौ बने तस्समिश्नम्यं ताल्यनं गतौ
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9468)
- **Original**: 9 तत्तु ताल्वन॑ दिव्य॑ धेनुकों नाम दानवः । मृगमांसकृताहार: सदाध्यास्ते खराकृति:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9469)
- **Original**: 2 तत्तु तालवन॑ पक्रफलसम्पत्समन्वितम्‌ । दृष्डा स्पृहान्विता गोपा: फलादानेउल्लुबन्बच: । 3 है राम हे कृष्ण सदा धेनुकेनैष रक्ष्यते । भूप्रदेशों यतस्तस्मात्पक्रानीमानि सन्ति वै
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9470)
- **Original**: 4 फलानि पद्य तालानां गन्धामोदितदीशि ये । बयमेतान्यभीप्साम: पात्यन्तां यदि रोचते
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9471)
- **Original**: 5 श्रीपयद्ञार उवाच इति गोपकुमाराणां श्रुत्वा सड्भूर्षणो वच: । एतत्कर्त्तव्यमित्युक्त्वा पातयामास तानि वे । कृष्णश्च पातयामास भुवि तानि फलानि वै
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9472)
- **Original**: 6 फलानां पततां झब्दमाकर्ण्य सुदुरासद: । आजगाम स दुष्टात्मा कोपाहतेयगर्दभ:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9473)
- **Original**: 7 प्रदभ्यामुभाभ्यां स तदा पश्चिमाभ्यां बलं बली । जघानोरसि ताभ्यां च स॒ च तेनाभ्यगृह्मयत
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9474)
- **Original**: 8 गृहीत्वा भ्रामयामास सो म्बरे गतजीवितम्‌। तस्मिन्नेव स चिक्षेप वेगेन तृणराजनि
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9475)
- **Original**: 9 ततः फलान्यनेकानि ताल्लाग्रानत्निपतन्खर: । पृथिव्यां पातयामास महावातो घनानिय
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9476)
- **Original**: 10 अन्यानथ सजातीयानागतान्दैत्यगर्दभान्‌ कृष्णश्रिक्षेप ताल्ाप्रे बलभद्रअन लीलया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9477)
- **Original**: 11 पृथ्वी पक्रैस्तालफलैस्तदा । 5224% 28 मैत्रेय शुशुभेडधिकम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9478)
- **Original**: 12 ततो गायो निराबाथास्तस्मिस्तालबने द्विज । नवह्ाष्पं सुर्ख चेरु्बन्न भुक्तमभूत्पुरा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9479)
- **Original**: उस दिव्य तालबनमें धेनुक गामक एक गधेके आकारवाला दैत्य मृगमांसका आहार करता हुआ सदा रहा करता था
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9480)
- **Original**: उस तालवनको पके फत्जेक् सम्मत्तिसे सम्पन्न देखकर उन्हें तोड़नेकी इचप्रसे गोपगण खोले
- **Translation**: 

---

