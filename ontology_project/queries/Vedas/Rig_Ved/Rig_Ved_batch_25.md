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

### Verse 1 (Rig Ved 0.481)
- **Original**: हे ऋगत्विजू ! आप हमारी रक्षा के लिये सवितादेवता की स्तुति करें । हम उनके लिए सोमयागादि कर्म सम्पन्न करना चाहते है । वे सवितादेब जलो को सुखाकर पुनः सहख््रों गुना बरसाने वाले हैं
- **Translation**: 

---

### Verse 2 (Rig Ved 0.482)
- **Original**: सौर शक्ति से ही जल के शोधन, वर्षण एवं शोषण की प्रक्रिया चलाने की बात विज्ञान सप्पत है ।] 215. विभक्तारं हवामहे वसोश्चित्रस्य राधस:। सवितार नृत्तक्षसम्‌
- **Translation**: 

---

### Verse 3 (Rig Ved 0.483)
- **Original**: समस्त प्राणियों के आश्रयभूत, विविध धर्नों के प्रदाता, मानवमात्र के प्रकाशक सूर्यदेव का हम आबाहन करते हैं
- **Translation**: 

---

### Verse 4 (Rig Ved 0.484)
- **Original**: 216. सखाय आ नि घीदत सविता स्तोम्यो नु न:ः। दाता राधांसि शुम्भति
- **Translation**: 

---

### Verse 5 (Rig Ved 0.485)
- **Original**: है मित्रो ! हम सब बैठकर सवितादेव की स्तुति करें । धन-ऐश्वर्य के दाता सूर्यदेव अत्यन्त शो भावमान हैं
- **Translation**: 

---

### Verse 6 (Rig Ved 0.486)
- **Original**: मं0 9 सू0 22 25 217. अग्ने पत्नीरिहा वह देवानामुशतीरुप । त्वष्टारं सोमपीतये
- **Translation**: 

---

### Verse 7 (Rig Ved 0.487)
- **Original**: है अग्निदेव ! यहाँ आने कौ अभिलाषा रखते वाली देवों की पत्लियों को यहाँ ले आएँ और त्वष्टादेव को भो सोमपान के निमित्त बुलाएँ
- **Translation**: 

---

### Verse 8 (Rig Ved 0.488)
- **Original**: 218 आ ग्ना अग्न इहावसे होत्रां यविष्ठ भारतीम्‌। वरूज्रीं थिषणां यह
- **Translation**: 

---

### Verse 9 (Rig Ved 0.489)
- **Original**: है अग्निदेव ! देवपत्लियों को हमारी सुरक्षा के नि्मित्त यहाँ ले आएँ । आप हमारी रक्षा के लिए अग्निपलो होत्रा, आदित्यपली भारती, बरणीय वाग्देवी घिषणा आदि देवियों को भी यहाँ ले आएँ
- **Translation**: 

---

### Verse 10 (Rig Ved 0.490)
- **Original**: 219. अभि नो देवीरबसा महः शर्मणा नृपत्नी:। अच्छिन्नपत्रा: सचन्ताम्‌
- **Translation**: 

---

### Verse 11 (Rig Ved 0.491)
- **Original**: अनवरुद्ध मार्ग वाली देव-पत्नियाँ मनुष्यों को ऐश्वर्य देने में समर्थ हैं। वे महान्‌ सुखों एवं रक्षण सामरथ्यों से युक्त होकर हमारी ओर अभिमुख हों
- **Translation**: 

---

### Verse 12 (Rig Ved 0.492)
- **Original**: 220. इहेन्द्राणीमुप हुये वरुणानीं स्वस्तये। अग्नायीं सोमपीतये
- **Translation**: 

---

### Verse 13 (Rig Ved 0.493)
- **Original**: अपने कल्याण के लिए एवं सोमपान के लिए हम इद्धाणों, वरुणपत्मी ( वकुणानी) और अग्निपतनी (अग्तायी) का आवाहन करते हैं
- **Translation**: 

---

### Verse 14 (Rig Ved 0.494)
- **Original**: 221. मही दौः पृथिवी च न इम॑ यज्ञ मिमिक्षताम्‌। पिपृतां नो भरीमभि:
- **Translation**: 

---

### Verse 15 (Rig Ved 0.495)
- **Original**: अति विस्तारयुक्त पृथ्वी और च्युलोक हमारे इस यज्ञकर्म को अपने-अपने आंशों द्वारा परिपूर्ण करें
- **Translation**: 

---

### Verse 16 (Rig Ved 0.496)
- **Original**: वे भरण-पोषण करने वाली सामग्रियों (सुख - साधनों ) से हम सभी को तृप्त करें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.497)
- **Original**: 222. तयोरिद्घृतवत्पयो विप्रा रिहन्ति धीतिभि:। गन्धर्वस्य ध्रुते पदे
- **Translation**: 

---

### Verse 18 (Rig Ved 0.498)
- **Original**: गंधर्वलोक के धुव स्थान में - आकाश और पृथ्वी के प्रध्य में अवस्थित घृत के समान ( सार रूप) जलो (पोषक प्रवाहों ) को ज्ञानी जन अपने विवेकयुक्त कमों ( प्रयासों ) द्वारा प्राप्त करते हैं
- **Translation**: 

---

### Verse 19 (Rig Ved 0.499)
- **Original**: 223 स्योना पृथिवि भवानृक्षरा निवेशनी । यच्छा न: शर्म सप्रथः
- **Translation**: 

---

### Verse 20 (Rig Ved 0.500)
- **Original**: हे पृथिवी देवि ! आप सुख देने वाली, बाधा हरने वालों और उत्तमवास देने वालो हैं। आप हमें विपुल परिष्राण में सुख प्रदान करें
- **Translation**: 

---

