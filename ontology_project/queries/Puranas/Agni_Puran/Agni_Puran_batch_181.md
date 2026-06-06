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

### Verse 1 (Agni Puran 0.3601)
- **Original**: प्रदान करनेवाला है। माघ मासके शुक्लपक्षकी
- **Translation**: 

---

### Verse 2 (Agni Puran 0.3602)
- **Original**: माघके कृष्णपक्षमें 'सर्वाप्ति-सप्तमी 'का व्रत सप्तमी तिथिको (अष्टदल अथवा द्वादशदल)
- **Translation**: 

---

### Verse 3 (Agni Puran 0.3603)
- **Original**: करना चाहिये। इससे सभी अभीष्ट वस्तुओंकी कमलका निर्माण करके उसमें भगवान्‌ सूर्यका
- **Translation**: 

---

### Verse 4 (Agni Puran 0.3604)
- **Original**: प्राप्ति होती है। फाल्गुनके कृष्णपक्षमें 'नन्द- पूजन करना चाहिये। इससे मनुष्य शोकरहित हो
- **Translation**: 

---

### Verse 5 (Agni Puran 0.3605)
- **Original**: सप्तमी 'का ब्रत करना चाहिये। मार्गशीर्षक शुक्ल- जाता है
- **Translation**: 

---

### Verse 6 (Agni Puran 0.3606)
- **Original**: पक्षमें "अपराजिता सप्तमी 'को भगवान्‌ सूर्यका भाद्रपद मासमें शुक्लपक्षकी सप्तमीको भगवान्‌
- **Translation**: 

---

### Verse 7 (Agni Puran 0.3607)
- **Original**: पूजन और ब्रत करना चाहिये। एक वर्षतक आदित्यका पूजन करनेसे समस्त अभीष्ट वस्तुओंकी
- **Translation**: 

---

### Verse 8 (Agni Puran 0.3608)
- **Original**: मार्गशीर्षक शुक्लपक्षका “पुत्रीया सप्तमी” ब्रत प्राप्ति होती है। पौषमासमें शुक्लपक्षकी सप्तमीको
- **Translation**: 

---

### Verse 9 (Agni Puran 0.3609)
- **Original**: स्त्रियोंकों पुत्र प्रदान करनेबाला है
- **Translation**: 

---

### Verse 10 (Agni Puran 0.3610)
- **Original**: इस प्रकार आदि आग्नेय महापुराणमें 'सक़्मीके व्रतोंका वर्ण” नामक एक सौँ बयासीवाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 11 (Agni Puran 0.3611)
- **Original**: + 88-49
- **Translation**: 

---

### Verse 12 (Agni Puran 0.3612)
- **Original**: 2&% कककिदक पतककककत 7 ऋ
- **Translation**: 

---

### Verse 13 (Agni Puran 0.3613)
- **Original**: 34340 88 66 एक सौ तिरासीवाँ अध्याय ##%#%#%#% कऋ # %
- **Translation**: 

---

### Verse 14 (Agni Puran 0.3614)
- **Original**: अष्टमी तिथिके ब्रत अग्निदेव कहते हैं-- वसिष्ठ ! अब मैं अष्टमीको किये जानेवाले ब्रतोंका वर्णन करूँगा। उनमें पहला रोहिणी नक्षत्रयुक्त अष्टमीका ब्रत है। भाद्रपद मासके कृष्णपक्षकी रोहिणी नक्षत्रसे युक्त अष्टमी तिथिको ही अर्धरात्रिके समय भगवान्‌ श्रीकृष्णका प्राकट्य हुआ था, इसलिये इसी अष्टमीको उनकी जयन्ती मनायी जाती है। इस तिथिकौ उपवास करनेसे मनुष्य सात जन्‍्मोंके किये हुए पापोंसे मुक्त हो जाता है
- **Translation**: 

---

### Verse 15 (Agni Puran 0.3615)
- **Original**: अतएव भाद्रपदके कृष्णपक्षको रोहिणीनक्षत्रयुक्त अष्टमीको उपवास रखकर भगवान्‌ श्रीकृष्णका पूजन करना चाहिये। यह भोग और मोक्ष प्रदान करनेवाला है
- **Translation**: 

---

### Verse 16 (Agni Puran 0.3616)
- **Original**: (पूजनकी विधि इस प्रकार है--) आबाहन-मन्त्र और नमस्कार आवाहयाम्यहं कृष्णं बलभद्वं च देवकीम्‌। बसुदेव॑ यशोदां गा: पूजयामि नमोःस्तु ते
- **Translation**: 

---

### Verse 17 (Agni Puran 0.3617)
- **Original**: योगाय योगपतये योगेशाय “नमो नमः। योगादिसम्भवायैव गोविन्दाय नमो. नमः
- **Translation**: 

---

### Verse 18 (Agni Puran 0.3618)
- **Original**: मैं श्रीकृष्ण, बलभद्र, देवको, वसुदेब, यशोदादेवी और गौओंका आवाहन एवं पूजन करता हूँ; आप सबको नमस्कार है। योगस्वरूप, योगपति एवं योगेश्वर श्रीकृष्णके लिये नमस्कार है। योगके आदिकारण, उत्तपत्तिस्थान श्रीगोविन्दके लिये बारंबार नमस्कार है'
- **Translation**: 

---

### Verse 19 (Agni Puran 0.3619)
- **Original**: तदनन्तर भगवान्‌ श्रीकृष्णको स्नान कराये और इस मन्त्रसे उन्हें अर्घध्धदान करें-- यज्ेश्वराय यज्ञाय यज्ञानां पतये नमः
- **Translation**: 

---

### Verse 20 (Agni Puran 0.3620)
- **Original**: अज्ञादिसम्भवायैव गोविन्दाय नमो नमः। “यज्ञेश्वर, यज्ञस्वरूप, यज्ञोंके अधिपति एवं यज्ञके आदि कारण श्रीगोविन्दको बारंबार नमस्कार है।' पुष्प-धूप गृहाण देव पुष्पाणि सुगन्धीनि प्रियाणि ते
- **Translation**: 

---

