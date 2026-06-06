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

### Verse 1 (Markende Puran 0.2121)
- **Original**: जिसमें प्रत्यक्ष दोष देखा गया है, ठस विषयके लिये भी हमारे गयमें ममताजनित आकर्षण यैंदा हो रहा है। महाघाग! हम दोनों समझदार हैं; तो भो हममें जो मोह पैदा हुआ है, बह क्तया,है 7 विवेकशून्य पुरुफक्ती भाँति मुझमें और इसमें भी यह मूह॒ता प्रत्यक्ष दिखायी देती है
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2122)
- **Original**: *+ मेथा ऋषिका राजा सुर और सपाधिकों भगवत्तीकी महिंसा सुनाना+ श89 हू. 8 ##4& 7 4477 मण0 7 1क 02 1:227:2:::55::566:&+# +### 44347 लब्ज्‌ 07 क7 कक क 10224 70 म
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2123)
- **Original**: 2 25554 22544 ऋषिरुवाच
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2124)
- **Original**: बलादाकृष्य मोहांय मह्यमाया प्रयच्छति। त्या चिसृज्यते विश्व जगदेत्रच्थराधरम
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2125)
- **Original**: सैषा प्रस॒श्ना घरदा नृणां भवत्ति पुक्तये। सा विद्या परमा मुक्तेर्तुभधूता सनातनी
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2126)
- **Original**: संसारयन्धहेनुश्च सैस सर्वेश्वरेश्वरी
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2127)
- **Original**: । ऋषि बोले ---
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2128)
- **Original**: महापाग ! विषयमार्गका ज्ञान क्तत्र जीवोंकों हैं
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2129)
- **Original**: इसी प्रकार लिफव भी सबके लिये अलग-अलग हैं। कुछ प्राणी दितमें नहीं देखते और दूसरे रातमें ही नहीं देखते
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2130)
- **Original**: तथा कुछ जीब ऐसे हैं, जो दिन और रात्रिमें भी बराबर ही देखते हैँ। यह ठीक है कि मनुष्य समझदार होते हैं; किंतु केवल वे ही ऐसे नहीं होते
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2131)
- **Original**: पशु-पक्षी और मृग आदि सभी प्राणी समझदार होते हैं। मनुष्योंकी समझ भी वैसी ही होती है, जैसी उन मृग और ज्ञानमस्ति सप्रस्तस्य जनन्‍्तोरखिंषयगोचरे
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2132)
- **Original**: पक्षियोंकी होती हैं
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2133)
- **Original**: तथा जैस्ली मनुप्योंकी विषयस महाभाग यात्ति चैर्व पृथक पृथक । दिवान्धा: प्राणिनः केचिद्रात्राअन्थास्तथापरे
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2134)
- **Original**: केचिद्धिवा तथा रात्रौ प्राणिनस्तुल्बदृष्टय:। ज्ञानिनों मनुजा: सर्त्य किंतु तन हि करेवलम्‌
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2135)
- **Original**: अतो हि ज्ञानिनः सर्वे पशुपक्षिमृगादवः। ज्ञान भव तन्मनुष्याणां यत्तेर्षा भृगपक्षिणाम्‌
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2136)
- **Original**: मनुष्याणां ज्ञ वत्तेषां तुल्यमन्यत्तथोभयो:। ज्ञानेंडपि सत्ति पश्चैतान्‌ पतड्भाज्छावचझ्जुघु
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2137)
- **Original**: कणमोक्षादुत्तान्मोहात्पीड्घमानानपि क्षुधरा। होती है, बैसी ही डन मृग-पक्षी आदिकी होती हैं। यह तथा अन्य ब्वातें भी प्रायः दोनोंमें समान ही हैं। समझ होनेपर भी इन पक्षिवोंक्रों तो देखो, ये स्व भूखसे पीड़ित होते हुए भी मोहबश बच्चोंकों चोचमें कितने चावसे अन्नके दाने डाल रहे हैं! नरश्रष् ! क्या तुम नहों देखते कि ये मनुष्य समज्ञदार होते हुए भी लोभजश अपने किये हुए. उपकारका बदला पानेके लिये पुत्रोंकी अभिलाषा करते हैं ? यद्यपि उन सबमें समझकी कमी नहों प्रानुषा प्रनुजत्याप्र साभिलाषाः सुतान्‌ प्रति
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2138)
- **Original**: है, तथापि वे संसारकी स्थिति (जन्म-मरणकी लोभात्मत्युपकाराय नन्वेतान्‌ कि न पश्यसि। तथापि ममतावरत्त मोहगर्ते निप्रातिता:।
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2139)
- **Original**: मह्वाप्रायाप्रभावेण संसारस्थितिकारिणों
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2140)
- **Original**: तन्नाज विस्मबः कार्यो योगनिद्रा जगत्पले:
- **Translation**: 

---

