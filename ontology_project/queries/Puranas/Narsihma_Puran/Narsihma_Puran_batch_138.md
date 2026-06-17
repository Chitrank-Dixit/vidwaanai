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

### Verse 1 (Narsihma Puran 0.2741)
- **Original**: श्च्च0 श्रीनरसिंहपुराण [ अध्याय 45 प्रतिज्ञा नैब कर्तव्या ददाम्येतत्तवेति वै। इति श्रुत्वा बच्रस्तस्थ बलिर्जबलवबतां बर:
- **Translation**: 

---

### Verse 2 (Narsihma Puran 0.2742)
- **Original**: 23 उत्ाच तां शुभां वाणी शुक्रमात्पपुरोहितम्‌। आगते वामने शुक्र यज्ञे मे मधुसूदने
- **Translation**: 

---

### Verse 3 (Narsihma Puran 0.2743)
- **Original**: 24 न शक्यते प्रतिख्यातुं दान॑ प्रति मया गुरो। अन्येषामपि जनन्‍्तूनापित्युक्त त्ते मयाधुना
- **Translation**: 

---

### Verse 4 (Narsihma Puran 0.2744)
- **Original**: 25 किं पुनर्वासुदेबस्थ आगतस्य तु शार्जिण:। त्वया विध्लो न कर्तव्यों बामनेउत्रागते द्विज
- **Translation**: 

---

### Verse 5 (Narsihma Puran 0.2745)
- **Original**: 26 यद्यदद्व्यं प्रार्थयते तत्तदद्रव्य ददाम्यहम्‌। कृतार्थो5हं मुनिश्रेष्ठ यद्यागच्छति वामन:
- **Translation**: 

---

### Verse 6 (Narsihma Puran 0.2746)
- **Original**: 27 इत्येव॑ वदतस्तस्य यज्ञशालां स वामनः। आगत्य प्रविवेशाथ प्रशशंस बलेम॑खम्‌
- **Translation**: 

---

### Verse 7 (Narsihma Puran 0.2747)
- **Original**: 28 ते दृष्ठा सहसा राजन्‌ राजा दैत्याधिपो बलि: । उपचारेण सम्पूज्य वाक्यमेतदुबाच ह
- **Translation**: 

---

### Verse 8 (Narsihma Puran 0.2748)
- **Original**: 29 यदहात्रार्थयसे मां त्व॑ देवदेव धनादिकम्‌। तत्सव॑ तव दास्यामि मां याचस्वाद्य वामन
- **Translation**: 

---

### Verse 9 (Narsihma Puran 0.2749)
- **Original**: 30 इत्युक्तो बामनस्तत्र नृपेत्न खलिना तदा। याचयामास देवेशो भूमेदेंहि पदत्रयम्‌
- **Translation**: 

---

### Verse 10 (Narsihma Puran 0.2750)
- **Original**: 31 प्रमाग्रिशरणार्थाय न मे3र्थ5स्ति प्रयोजनम्‌। इत्युक्तो बामनेनाथ बलि: प्राह चर वामनम्‌
- **Translation**: 

---

### Verse 11 (Narsihma Puran 0.2751)
- **Original**: 32 पदत्रयेण चेत्तृप्तिमया दत्त पदत्रयम्‌। एवमुक्ते तु खलिना बामनो ब्लिमब्बवीत्‌
- **Translation**: 

---

### Verse 12 (Narsihma Puran 0.2752)
- **Original**: 33 दीयतां मे करे त्तोयं यदि दत्त पदत्रयम्‌। इत्युक्तो देबदेबेन तदा तत्र स्वयं बलि:
- **Translation**: 

---

### Verse 13 (Narsihma Puran 0.2753)
- **Original**: 34 “मैं आपको यह वस्तु देता हूँ" यों कहकर कुछ देनेकी प्रतिज्ञा न करना!
- **Translation**: 

---

### Verse 14 (Narsihma Puran 0.2754)
- **Original**: 20--225;
- **Translation**: 

---

### Verse 15 (Narsihma Puran 0.2755)
- **Original**: डनकी यह बज्रात सुनकर बलतानोंमें श्रेष्ठ बलिने अपने पुरोहित शुक्राचार्यजीसे यह सुन्दर बात कही-- “गुरुदेव शुक्र! यज्ञमें मधुसूदन भगवान्‌ वामनके पधारनेपर मैं उन्हें कुछ भी देनेसे इनकार नहीं कर सकता। अभी- अभी मैं आपसे कह चुका हूँ कि दूसरे प्राणी भी यदि मुझसे कुछ याचना करेंगे तो मैं उन्हें वह वस्तु देनेसे इसकार नहीं कर सकता; फिर शा्ड़र धनुष धारण करनेवाले साक्षात्‌ भगवान्‌ विष्णु (वासुदेव)मेंरे यज्ञमें पधारें और मैं उनकी मुँहमाँगी वस्तु उन्हें देनेसे इनकार कर दूँ, यह कैसे सम्भव होगा? ब्राह्मणदेव! यहाँ भगवान्‌ बामनके पदार्पण करनेपर आप उनके कार्यमें व्रिज्न न डालियेगा। ये जो-जो द्रव्य साँगेंगे, वही-यही मैं उन्हें दूँगा। मुनिश्रेष्ठ यदि सचमुच ही यहाँ भगवान्‌ यामन पधार रहे हैं तो मैं कृतार्थ हो गया'
- **Translation**: 

---

### Verse 16 (Narsihma Puran 0.2756)
- **Original**: 23--27
- **Translation**: 

---

### Verse 17 (Narsihma Puran 0.2757)
- **Original**: राजा जलि जब इस प्रकार कह रहे थे, उसों समय यामनजीने आकर यज्ञशालामें प्रवेश किया और ये उनके उस यज्ञकी प्रशंसा करने लगे। राजन्‌! उन्हें देखते हो दैत्याधिपति राजा बलिने सहसा उठकर पूजन-सामग्रियोंसे उनकी पूजा की, फिर इस प्रकार कहा--' देवदेव
- **Translation**: 

---

### Verse 18 (Narsihma Puran 0.2758)
- **Original**: आप धन आदि जो-जो वस्तु माँगेंगे, वह सब मैं आपको दूँगा; इसलिये वामनजी! आज आप मुझसे याचतरा कीजिये '
- **Translation**: 

---

### Verse 19 (Narsihma Puran 0.2759)
- **Original**: 28--30
- **Translation**: 

---

### Verse 20 (Narsihma Puran 0.2760)
- **Original**: “नूपेन्द्र! बलिके यों कहनेपर उस समय देवेश्वर भगन्नानू ज्रामनने उनसे यही याचना को कि मुझे अग्निशालाके लिये केवल त्तीन पग भूमि दीजिये, मुझे धनकी आवश्यकता नहीं है'
- **Translation**: 

---

