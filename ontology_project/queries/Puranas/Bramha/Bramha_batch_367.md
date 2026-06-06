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

### Verse 1 (Bramha 0.7321)
- **Original**: शाठ्येनापि नशा नित्य॑ ये स्मरन्ति जनार्दनम्‌ । तैईपि यान्ति तनुं त्यक्त्वा विष्णुलोकमनामयम्‌
- **Translation**: 

---

### Verse 2 (Bramha 0.7322)
- **Original**: अत्यन्तक्रोधसक्तो5प.. कदाचित्कीर्तयेद्धरिम। सोउपि दोषफक्षयान्मुक्ति लभेच्चेदिपतिर्यथा
- **Translation**: 

---

### Verse 3 (Bramha 0.7323)
- **Original**: 82-89) ........ुु........नन-न तन «मम. लम_भनमनम न» 3+--.-.-+-मनमममन्‍ननननननननन_ाा मन “"“++ नमन न ह $
- **Translation**: 

---

### Verse 4 (Bramha 0.7324)
- **Original**: धर्मकी महिमा एवं अधर्मकी गतिका निरूपण तथा अन्नदानका माह॒त्म्य मुनियोने कहा-- भगवन्‌! आप सम्पूर्ण धर्मोके
- **Translation**: 

---

### Verse 5 (Bramha 0.7325)
- **Original**: सहायक बताया गया है। बहुत-से शास्त्रोंका ज्ञाता ज्ञाता तथा सब शास्त्रोंके ज्ञानमें निपुण हैं। कृपया
- **Translation**: 

---

### Verse 6 (Bramha 0.7326)
- **Original**: मनुष्य भी लोभ, मोह, घृणा अथवा भयसे मोहित बताइये पिता, माता, पुत्र, गुरु, जातिवाले, सम्बन्धी
- **Translation**: 

---

### Verse 7 (Bramha 0.7327)
- **Original**: होकर दूसरेके लिये न करने योग्य कार्य भी कर और मित्रवर्ग-इनमेंसे कौन मरनेवाले प्राणीका
- **Translation**: 

---

### Verse 8 (Bramha 0.7328)
- **Original**: डालता है। धर्म, अर्थ और काम--तीनों ही इस विशेष सहायक होता है? लोग तो मृतकके शरीरकों
- **Translation**: 

---

### Verse 9 (Bramha 0.7329)
- **Original**: जीवनके फल हैं। अधर्म-त्यागपूर्वक इन तीनोंकी काठ और मिट्टीके ढेलेकी भाँति छोड़कर चल देते
- **Translation**: 

---

### Verse 10 (Bramha 0.7330)
- **Original**: प्राप्ति करनी चाहिये।* हैं, फिर परलोकमें कौन उसके साथ जाता है?
- **Translation**: 

---

### Verse 11 (Bramha 0.7331)
- **Original**: मुनियोने कहा-- भगवन्‌
- **Translation**: 

---

### Verse 12 (Bramha 0.7332)
- **Original**: आपका यह धर्मयुक्त व्यासजी बोले--विप्रवरो ! प्राणी अकेला ही
- **Translation**: 

---

### Verse 13 (Bramha 0.7333)
- **Original**: बचन, जो परम कल्याणका साधन है, हमने जन्म लेता, अकेला ही मरता, अकेला ही दुर्गम
- **Translation**: 

---

### Verse 14 (Bramha 0.7334)
- **Original**: सुना। अब हम यह जानना चाहते हैं कि यह संकटोंको पार करता और अकेला ही दुर्गतिमें
- **Translation**: 

---

### Verse 15 (Bramha 0.7335)
- **Original**: शरीर किन तत्त्वोंका समूह है। मनुष्योंका मरा पड़ता है। पिता, माता, भ्राता, पुत्र, गुरु, जातिवाले,
- **Translation**: 

---

### Verse 16 (Bramha 0.7336)
- **Original**: हुआ शरीर तो स्थूलसे सूक्ष्म-अव्यक्तभावको सम्बन्धी तथा मित्रवर्ग-इनमेंसे कोई भी मरनेवालेका
- **Translation**: 

---

### Verse 17 (Bramha 0.7337)
- **Original**: प्राप्त हों जाता है, वह नेत्नोंका विषय नहीं रह साथ नहीं देता। घरके लोग मृत व्यक्तिके शरीरकों
- **Translation**: 

---

### Verse 18 (Bramha 0.7338)
- **Original**: जाता; फिर धर्म कैसे उसके साथ जाता है? काठ और मिट्टीके ढेलेकी भाँति त्याग देते और
- **Translation**: 

---

### Verse 19 (Bramha 0.7339)
- **Original**: व्यासजी बोले--पृथ्वी, वायु, आकाश, जल, दो घड़ी रोकर उससे मुँह मोड़कर चले जाते हैं।
- **Translation**: 

---

### Verse 20 (Bramha 0.7340)
- **Original**: तेज, मन, बुद्धि और आत्मा-ये सदा साथ रहकर वे सब लोग तो त्याग देते हैं, किन्तु धर्म उसका ! धर्मपर दृष्टि रखते हैं। ये समस्त प्राणियोंके शुभाशुभ त्याग नहों करता। वह अकेला ही जोवके साथ
- **Translation**: 

---

