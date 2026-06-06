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

### Verse 1 (Vishnu Puran 0.7301)
- **Original**: तद्च विपरीत कुर्वत्यास्तवातिरौद्राख्रधारणपालननिष्: क्षत्रियाचार: पुत्रों भविष्यति तस्थाश्रोप- जामरुचित्राह्मणाचार इत्याकण्यैंव सा तस्य पादौ जग्राह
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7302)
- **Original**: प्रणिपत्य चैनमाह
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7303)
- **Original**: भगवन्मयैतदज़ानादनुष्ठित॑ प्रसाद॑ मे कुरु मैव॑विध: पुत्रो भवतु कापमेवंविध: पौत्रो भवत्वित्यक्त मुनिरप्याह
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7304)
- **Original**: एवमसस्त्विति
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7305)
- **Original**: । उसे भृगुपुत्र ऋचीकने वरण किया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7306)
- **Original**: गाधिने अति क्रोघी और अति वृद्ध ब्राह्मणकों कन्या न देनेकी इच्छासे ऋचीकसे कन्याके मूल्यमें जो चन्द्रमाके समान कान्तिमान्‌ अर पवनके तुल्य बेगबान्‌ हों, ऐसे एक सहस्तर श्यामकर्ण घोड़े माँग
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7307)
- **Original**: किन्तु महर्षि ऋचीकने अश्वतीर्थसे उत्पन्न हुए जैसे एक सहस घोडे उन्हें बरुणसे लेकर दे दिये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7308)
- **Original**: तब क्रचीकने ठस कन्यासे बिबाह किया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7309)
- **Original**: [ तदुपराज्त एक समय ] उन्होंने सच्तानकी कामनासे सत्यवतीके ल्त्ये चरू (यज्जीय खीर) तैयार किया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7310)
- **Original**: और उसीके द्वारा प्रसन्न किये जानेपर एक क्षत्रियश्रेष्ठ पुत्र॒की उत्पत्तिके लिये एक और चरु उसकी माताके लिये भी बनाया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7311)
- **Original**: और “यह चर तुप्हारे लिये है तथा यह तम्हरी माताके लिये--इनका तम य्रथोद्चित उप्योग करना'--ऐसा कहकर जे बनको चले गये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7312)
- **Original**: उनका उपयोग करते समय सत्यबतीकी माताने उससे कहा--
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7313)
- **Original**: “बेटी ! सभी लोग अपने ही लिये सबसे अधिक गुणवान्‌ पुत्र चाहते हैं, अपनी पत्रोंके भाईके गुणोमें किसीकी भी विज्ेष रुचि नहीं होती
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7314)
- **Original**: अतः तू अपना चरु तो मुझे दे दे और मेरा तू ले ले; क्योंकि मेरे पुत्रको तो सम्पूर्ण भूमण्डलका पालन करना होगा और बाह्मणकुमारकों तो बल, वोर्य तथा सम्पत्ति आदिसे लेना ही क्‍या है ।'' ऐसा कहनेपर सत्यकतीने अपना चरूु अपनी मालाको दे दिया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7315)
- **Original**: वनसे ल्वैटनेपर ऋषिने सत्यवतीको देखकर कहा-- “अरी पाषिनि ! तुने ऐसा क्‍या अकर्य किया है जिससे तेरा झरीर ऐसा भयानक प्रतीत होता है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7316)
- **Original**: अबइ्य हो तुने अपनी माताके छ़िये तैयार किये चरूका उपयोग किया हे, सो ठीक नहीं है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7317)
- **Original**: मैंने उसमें सम्पूर्ण ऐश्वर्य, पराक्रम, झूस्ता और यलूकी सम्पत्तिका आरोपण किया था तथा तेरेमें शान्ति, ज्ञान, तितिक्षा आदि सम्पूर्ण ब्राह्मणोचित गुणोंका समाबेश् किया था
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7318)
- **Original**: उनका खिपरीत उपयोग करनेसे तेरे अति भयानक अख्न-दास्मधारी पालन-कर्ममें_ तत्पर क्षत्रियके समान आचरणबात्य पुत्र होगा और उसके हात्तिप्रिय ग्राह्मणाचारयुक्त पुप्र होगा।'” यह सुनते ही सत्यवतीने उनके चरण फ्कड़ छिये और प्रणाम करके कहा---
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7319)
- **Original**: “भगवन्‌ ! अज्ञानसे ही मैंने ऐसा किया है, अत प्रसन्न होइये और ऐसा कीजिये जिससे मेरा पुष्र ऐसा न हो, भरे ही पौष् ऐसा हो जाय !” इसपर सुनिने कहा--- ऐसा ही हो ।'
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7320)
- **Original**: आ<8 ] अनन्तरं चर सा जमदभग्रिमजीजनत्‌
- **Translation**: 

---

