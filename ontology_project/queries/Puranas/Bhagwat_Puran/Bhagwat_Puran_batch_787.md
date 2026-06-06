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

### Verse 1 (Bhagwat Puran 0.15721)
- **Original**: दूध या खीरका मौन भोजन करे। नित्य ब्रह्मचर्यका पालन और धूमिपर शयन करे, क्रोध और लोभ आदिको त्याग दे
- **Translation**: 

---

### Verse 2 (Bhagwat Puran 0.15722)
- **Original**: प्रतिदिन कथाके अन्तमें कीर्तन करें और कथासमाप्तिके दिन रात्रिमें जागरण करे । समाप्ति होनेपर ब्राह्मणोंकों भोजन कराकर उन्हें दक्षिणासे सम्तुष्ट करें
- **Translation**: 

---

### Verse 3 (Bhagwat Puran 0.15723)
- **Original**: कथाबाचक गुरुको बस््र, आभूषण आदि देकर गौ भी अर्पण करे । इस प्रकार विधि-बिधान पूर्ण करनेपर मनुष्यको स्त्री, घर, पुत्र, राज्य और घन आदि जो-जो उसे अभीष्ट होता है, वह सब मनोवाब्छित फल ग्राप्त होता है। परन्तु सकामभाव बहुत बड़ी बिडम्बना है, वह श्रीमद्भागवतकी कथामें शोभा नहीं देता
- **Translation**: 

---

### Verse 4 (Bhagwat Puran 0.15724)
- **Original**: श्रीशुकदेवजीके मुखसे कहा हुआ यह श्रीमद्धागवतशास््र तो कलियुगमें साक्षात्‌ श्रीकृष्णकी प्राप्ति करानेवाला और नित्य प्रेमानन्दरूप फल प्रदान करनेवाला है
- **Translation**: 

---

### Verse 5 (Bhagwat Puran 0.15725)
- **Original**: के केक केक श्रीमद्धागवतमाहात्म्य समाप्त
- **Translation**: 

---

### Verse 6 (Bhagwat Puran 0.15726)
- **Original**: हरि: 3» तत्सत्‌
- **Translation**: 

---

### Verse 7 (Bhagwat Puran 0.15727)
- **Original**: श्रीहरि:
- **Translation**: 

---

### Verse 8 (Bhagwat Puran 0.15728)
- **Original**: श्रीमद्भागवतकी आरती आरति अतिपावन पुरानकी । धर्म-भक्ति-विज्ञान-खानकी महापुरान भागवत निरमल । शुक-मुख-बिगलित निगम-कल्प-फल
- **Translation**: 

---

### Verse 9 (Bhagwat Puran 0.15729)
- **Original**: परमानन्द-सुधा-रसमय कल
- **Translation**: 

---

### Verse 10 (Bhagwat Puran 0.15730)
- **Original**: लीला-रति-रस रस-निधानकी._
- **Translation**: 

---

### Verse 11 (Bhagwat Puran 0.15731)
- **Original**: आ0 कलि-मल-मथनि त्रिताप-निवारिनि । जन्म-मृत्युमय भव-भय-हारिनि । सेवत सतत सकल सुखकारिनि। सुमहोषधि हरि-चरित-गानकी
- **Translation**: 

---

### Verse 12 (Bhagwat Puran 0.15732)
- **Original**: ओ0 विषय-विलास-विमोह-विनाशिनि । विमल विराग विवेक विकाशिनि
- **Translation**: 

---

### Verse 13 (Bhagwat Puran 0.15733)
- **Original**: भगवत्तत्त्व-रहस्य प्रकाशिनि । परम ज्योति परसात्म-ज्ञानकी
- **Translation**: 

---

### Verse 14 (Bhagwat Puran 0.15734)
- **Original**: आ0 परमहंस-मुनि-मन उल्लासिनि । रसिक-हृदय रस-रास-विलासिनि । भुक्ति, मुक्ति, रतिप्रेम सुदासिनि। कथा अकिद्लनप्रिय सुजानकी
- **Translation**: 

---

### Verse 15 (Bhagwat Puran 0.15735)
- **Original**: आ0 नह जय की औ >>
- **Translation**: 

---

